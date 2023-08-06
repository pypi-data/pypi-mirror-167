from typing import Any, Callable, Iterable, Optional, Union

from docdeid.annotation.annotation import Annotation
from docdeid.annotation.annotation_processor import BaseAnnotationProcessor
from docdeid.annotation.redactor import BaseRedactor
from docdeid.tokenizer.token import Token
from docdeid.tokenizer.tokenizer import BaseTokenizer


class Document:
    """A document contains information on a single text, be it a phrase, sentence or paragraph."""

    def __init__(
        self,
        text: str,
        tokenizer: Optional[BaseTokenizer] = None,
        meta_data: Optional[dict] = None,
    ):

        self._text = text
        self._annotations = set()

        self._tokenizer = tokenizer
        self._meta_data = meta_data

        self._tokens = None
        self._deidentified_text = None

    @property
    def text(self) -> str:
        """The documents text."""
        return self._text

    @property
    def tokens(self) -> list[Token]:
        """
        The documents' tokens, with lazy evaluation.

        Returns: A list of Token.

        """

        if self._tokens is None:
            self._tokens = self._tokenizer.tokenize(self._text)

        return self._tokens.copy()

    @property
    def annotations(self) -> set[Annotation]:
        """
        The documents' annotations.

        Returns: A set of Annotation.

        """
        return self._annotations.copy()

    def get_annotations_sorted(
        self,
        by: list[str],
        callbacks: dict[str, Callable] = None,
        deterministic: bool = True,
    ) -> list[Annotation]:

        return sorted(
            list(self._annotations),
            key=lambda x: x.get_sort_key(
                by=by, callbacks=callbacks, deterministic=deterministic
            ),
        )

    @property
    def deidentified_text(self) -> str:
        """
        The documents' deidentified text, if present.

        Returns: The deidentified text.

        """

        return self._deidentified_text

    def get_meta_data(self) -> dict:
        return self._meta_data

    def get_meta_data_item(self, key: str) -> Union[Any, None]:
        """
        Get an item from the documents' meta data.

        Args:
            key: The item key.

        Returns: The item, if present.

        """

        if key not in self._meta_data:
            return None

        return self._meta_data[key]

    def add_annotation(self, annotation: Annotation):
        """
        Add annotation to this document.

        Args:
            annotation: The annotation to be added.

        """
        self._annotations.add(annotation)

    def add_annotations(self, annotations: Iterable[Annotation]):
        """
        Add multiple annotations to this document.

        Args:
            annotations: The annotations to be added, in any iterable.

        """

        for annotation in annotations:
            self._annotations.add(annotation)

    def apply_annotation_processor(self, processor: BaseAnnotationProcessor):
        """
        Apply an annotation processor to this document.

        Args:
            processor: The processor to be applied.

        """

        if not isinstance(processor, BaseAnnotationProcessor):
            raise TypeError(
                f"Expected an object of type AnnotationProcessor, but received {type(processor)}"
            )

        if len(self._annotations) == 0:
            return

        self._annotations = processor.process(self._annotations, self.text)

    def apply_redactor(self, redactor: BaseRedactor):
        """
        Apply a redactor to this document, initializing the deidentified text.
        Args:
            redactor: The redactor to be applied.

        """

        if not isinstance(redactor, BaseRedactor):
            raise TypeError(
                f"Expected an object of type Redactor, but received {type(redactor)}"
            )

        self._deidentified_text = redactor.redact(self.text, list(self._annotations))
