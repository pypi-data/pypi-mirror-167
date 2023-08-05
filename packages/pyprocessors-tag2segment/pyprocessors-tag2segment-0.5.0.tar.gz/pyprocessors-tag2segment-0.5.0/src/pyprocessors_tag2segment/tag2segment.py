from typing import Type, List, cast

from pydantic import BaseModel, Field
from pymultirole_plugins.util import comma_separated_to_list
from pymultirole_plugins.v1.processor import ProcessorParameters, ProcessorBase
from pymultirole_plugins.v1.schema import Document, Sentence


class Tag2SegmentParameters(ProcessorParameters):
    segmentation_labels: List[str] = Field(
        None,
        description="""The list of possible label names to use as beginning of segment tags, all if empty. For example `\"bos\"`""",
        extra="label"
    )


class Tag2SegmentProcessor(ProcessorBase):
    """Tag2Segment processor ."""

    def process(
        self, documents: List[Document], parameters: ProcessorParameters
    ) -> List[Document]:
        params: Tag2SegmentParameters = cast(
            Tag2SegmentParameters, parameters
        )
        segmentation_labels = params.segmentation_labels or []
        for document in documents:
            if document.annotations:
                segmentation_annots = [a for a in document.annotations if len(segmentation_labels) == 0 or a.labelName in segmentation_labels]
                indexes = sorted([a.start for a in segmentation_annots])
                start = 0
                sentences = []
                for i in indexes:
                    if i > start:
                        sentences.append(Sentence(start=start, end=i-1))
                        start = i
                if i < len(document.text):
                    sentences.append(Sentence(start=i, end=len(document.text)))
                document.sentences = sentences
        return documents

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return Tag2SegmentParameters
