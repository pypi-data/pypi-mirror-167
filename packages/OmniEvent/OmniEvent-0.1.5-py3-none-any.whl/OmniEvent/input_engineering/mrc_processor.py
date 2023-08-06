import json
import logging

from tqdm import tqdm
from .base_processor import (
    EAEDataProcessor,
    EAEInputExample,
    EAEInputFeatures
)
from .mrc_converter import read_query_templates
from .input_utils import get_words, get_left_and_right_pos, get_word_ids
from collections import defaultdict

logger = logging.getLogger(__name__)


class EAEMRCProcessor(EAEDataProcessor):
    """Data processor for Machine Reading Comprehension (MRC) for event argument extraction.

    Data processor for Machine Reading Comprehension (MRC) for event argument extraction. The class is inherited from
    the `EAEDataProcessor` class, in which the undefined functions, including `read_examples()` and
    `convert_examples_to_features()` are implemented; a new function entitled `remove_sub_word()` is defined to remove
    the annotations whose word is a sub-word, the rest of the attributes and functions are multiplexed from the
    `EAEDataProcessor` class.
    """

    def __init__(self,
                 config,
                 tokenizer,
                 input_file: str,
                 pred_file: str,
                 is_training: bool = False) -> None:
        """Constructs a `EAEMRCProcessor`."""
        super().__init__(config, tokenizer, pred_file, is_training)
        self.read_examples(input_file)
        self.convert_examples_to_features()

    def read_examples(self,
                      input_file: str) -> None:
        """Obtains a collection of `EAEInputExample`s for the dataset."""
        self.examples = []
        self.data_for_evaluation["golden_arguments"] = []
        trigger_idx = 0
        query_templates = read_query_templates(self.config.prompt_file,
                                               translate=self.config.dataset_name == "ACE2005-ZH")
        template_id = self.config.mrc_template_id
        language = self.config.language
        with open(input_file, "r", encoding="utf-8") as f:
            for idx, line in enumerate(tqdm(f.readlines(), desc="Reading from %s" % input_file)):
                item = json.loads(line.strip())
                text = item["text"]
                words = get_words(text=text, language=language)
                if "events" in item:
                    for event in item["events"]:
                        for trigger in event["triggers"]:
                            pred_type = self.get_single_pred(trigger_idx, input_file, true_type=event["type"])
                            trigger_idx += 1

                            # Evaluation mode for EAE
                            # If predicted event type is NA:
                            #   in [default] and [loose] modes, we don't consider the trigger
                            #   in [strict] mode, we consider the trigger
                            if self.config.eae_eval_mode in ["default", "loose"] and pred_type == "NA":
                                continue

                            # golden label for the trigger
                            arguments_per_trigger = dict(id=trigger_idx-1,
                                                         arguments=[],
                                                         pred_type=pred_type,
                                                         true_type=event["type"])
                            for argument in trigger["arguments"]:
                                arguments_per_role = dict(role=argument["role"], mentions=[])
                                for mention in argument["mentions"]:
                                    left_pos, right_pos = get_left_and_right_pos(text, mention, language)
                                    arguments_per_role["mentions"].append({
                                        "position": [left_pos, right_pos - 1]
                                    })
                                arguments_per_trigger["arguments"].append(arguments_per_role)
                            self.data_for_evaluation["golden_arguments"].append(arguments_per_trigger)

                            if pred_type == "NA":
                                assert self.config.eae_eval_mode == "strict"
                                # in strict mode, we add the gold args for the trigger but do not make predictions
                                continue

                            trigger_left, trigger_right = get_left_and_right_pos(text, trigger, language)

                            for role in query_templates[pred_type].keys():
                                query = query_templates[pred_type][role][template_id]
                                query = query.replace("[trigger]", self.tokenizer.tokenize(trigger["trigger_word"])[0])
                                query = get_words(text=query, language=language)
                                if self.is_training:
                                    no_answer = True
                                    for argument in trigger["arguments"]:
                                        if argument["role"] not in query_templates[pred_type]:
                                            logger.warning(
                                                "No template for %s in %s" % (argument["role"], pred_type))
                                            pass
                                        if argument["role"] != role:
                                            continue
                                        no_answer = False
                                        for mention in argument["mentions"]:
                                            left_pos, right_pos = get_left_and_right_pos(text, mention, language)
                                            example = EAEInputExample(
                                                example_id=trigger_idx-1,
                                                text=words,
                                                pred_type=pred_type,
                                                true_type=event["type"],
                                                input_template=query,
                                                trigger_left=trigger_left,
                                                trigger_right=trigger_right,
                                                argument_left=left_pos,
                                                argument_right=right_pos - 1,
                                                argument_role=role,
                                            )
                                            self.examples.append(example)
                                    if no_answer:
                                        example = EAEInputExample(
                                            example_id=trigger_idx-1,
                                            text=words,
                                            pred_type=pred_type,
                                            true_type=event["type"],
                                            input_template=query,
                                            trigger_left=trigger_left,
                                            trigger_right=trigger_right,
                                            argument_left=-1,
                                            argument_right=-1,
                                            argument_role=role,
                                        )
                                        self.examples.append(example)
                                else:
                                    # one instance per query
                                    example = EAEInputExample(
                                        example_id=trigger_idx-1,
                                        text=words,
                                        pred_type=pred_type,
                                        true_type=event["type"],
                                        input_template=query,
                                        trigger_left=trigger_left,
                                        trigger_right=trigger_right,
                                        argument_left=-1,
                                        argument_right=-1,
                                        argument_role=role,
                                    )
                                    self.examples.append(example)
                    # negative triggers
                    for neg_trigger in item["negative_triggers"]:
                        pred_type = self.get_single_pred(trigger_idx, input_file, true_type="NA")
                        trigger_idx += 1

                        if self.config.eae_eval_mode == "loose":
                            continue
                        elif self.config.eae_eval_mode in ["default", "strict"]:
                            if pred_type == "NA":
                                continue
                            trigger_left, trigger_right = get_left_and_right_pos(text, neg_trigger, language)

                            for role in query_templates[pred_type].keys():
                                query = query_templates[pred_type][role][template_id]
                                query = query.replace("[trigger]",
                                                      self.tokenizer.tokenize(neg_trigger["trigger_word"])[0])
                                query = get_words(text=query, language=self.config.language)
                                # one instance per query
                                example = EAEInputExample(
                                    example_id=trigger_idx-1,
                                    text=words,
                                    pred_type=pred_type,
                                    true_type="NA",
                                    input_template=query,
                                    trigger_left=trigger_left,
                                    trigger_right=trigger_right,
                                    argument_left=-1,
                                    argument_right=-1,
                                    argument_role=role,
                                )
                                self.examples.append(example)

                        else:
                            raise ValueError("Invalid eae_eval_mode: %s" % self.config.eae_eval_mode)
                else:
                    for candi in item["candidates"]:
                        trigger_left, trigger_right = get_left_and_right_pos(text, candi, language)

                        pred_type = self.event_preds[trigger_idx]
                        trigger_idx += 1
                        if pred_type != "NA":
                            for role in query_templates[pred_type].keys():
                                query = query_templates[pred_type][role][template_id]
                                query = query.replace("[trigger]", self.tokenizer.tokenize(candi["trigger_word"])[0])
                                query = get_words(text=query, language=language)
                                # one instance per query
                                example = EAEInputExample(
                                    example_id=trigger_idx-1,
                                    text=words,
                                    pred_type=pred_type,
                                    true_type="NA",
                                    input_template=query,
                                    trigger_left=trigger_left,
                                    trigger_right=trigger_right,
                                    argument_left=-1,
                                    argument_right=-1,
                                    argument_role=role,
                                )
                                self.examples.append(example)
            if self.event_preds is not None:
                assert trigger_idx == len(self.event_preds)

    def convert_examples_to_features(self) -> None:
        """Converts the `EAEInputExample`s into `EAEInputFeatures`s."""
        self.input_features = []
        self.data_for_evaluation["text_range"] = []
        self.data_for_evaluation["text"] = []

        for example in tqdm(self.examples, desc="Processing features for MRC"):
            # context
            input_context = self.tokenizer(example.text,
                                           truncation=True,
                                           max_length=self.config.max_seq_length,
                                           is_split_into_words=True)
            # template
            input_template = self.tokenizer(example.input_template,
                                            truncation=True,
                                            padding="max_length",
                                            max_length=self.config.max_seq_length,
                                            is_split_into_words=True)

            input_context = self.remove_sub_word(self.tokenizer, input_context, example.text)
            # concatenate
            input_ids = input_context["input_ids"] + input_template["input_ids"]
            attention_mask = input_context["attention_mask"] + input_template["attention_mask"]
            token_type_ids = [0] * len(input_context["input_ids"]) + [1] * len(input_template["input_ids"])
            # truncation
            input_ids = input_ids[:self.config.max_seq_length]
            attention_mask = attention_mask[:self.config.max_seq_length]
            token_type_ids = token_type_ids[:self.config.max_seq_length]
            # output labels
            start_position = 0 if example.argument_left == -1 else example.argument_left + 1
            end_position = 0 if example.argument_right == -1 else example.argument_right + 1
            # data for evaluation
            text_range = dict()
            text_range["start"] = 1
            text_range["end"] = text_range["start"] + sum(input_context["attention_mask"][1:])
            self.data_for_evaluation["text_range"].append(text_range)
            self.data_for_evaluation["text"].append(example.text)
            # features
            features = EAEInputFeatures(
                example_id=example.example_id,
                input_ids=input_ids,
                attention_mask=attention_mask,
                token_type_ids=token_type_ids,
                argument_left=start_position,
                argument_right=end_position,
            )
            self.input_features.append(features)

    @staticmethod
    def remove_sub_word(tokenizer, inputs, word_list):
        """Removes the annotations whose word is a sub-word."""
        outputs = defaultdict(list)
        pre_word_id = -1
        for token_id, word_id in enumerate(get_word_ids(tokenizer, inputs, word_list)):
            if token_id == 0 or (word_id != pre_word_id and word_id is not None):
                for key in inputs:
                    outputs[key].append(inputs[key][token_id])
            pre_word_id = word_id
        return outputs
