import json
from pathlib import Path

from pymultirole_plugins.v1.schema import Document, DocumentList
from pyprocessors_tag2segment.tag2segment import (
    Tag2SegmentProcessor,
    Tag2SegmentParameters,
)


def test_model():
    model = Tag2SegmentProcessor.get_model()
    model_class = model.construct().__class__
    assert model_class == Tag2SegmentParameters


def test_tag2segment():
    testdir = Path(__file__).parent
    source = Path(testdir, "data/wescreen_annote-documents.json")
    with source.open("r") as fin:
        docs = json.load(fin)
        original_docs = [Document(**doc) for doc in docs]
    original_segs = [len(doc.sentences) for doc in original_docs]
    processor = Tag2SegmentProcessor()
    parameters = Tag2SegmentParameters()
    docs = processor.process(original_docs, parameters)
    tag2segmented: Document = docs[0]
    assert len(tag2segmented.sentences) < original_segs[0]
    result = Path(testdir, "data/wescreen_annote-documents-segmented.json")
    dl = DocumentList(__root__=docs)
    with result.open("w") as fout:
        print(dl.json(exclude_none=True, exclude_unset=True, indent=2), file=fout)
