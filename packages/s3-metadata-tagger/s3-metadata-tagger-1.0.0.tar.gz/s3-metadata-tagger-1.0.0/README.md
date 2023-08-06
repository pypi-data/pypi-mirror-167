# AWS S3 Metadata Tagger
The S3 Metadata tagger adds information in the form of metadata to files saved in S3.

To do this, the central handler takes a file location and a metadata extracting function.
It first checks whether the file already contains the requested information via a `HEAD` request.
If it does not, it downloads the file, invokes extracting function, and adds the metadata to
the s3 object with a inplace `COPY, MetadataDirective="REPLACE"` operation.

This package comes with two optional variants for metadata extraction:
* pdf: for determining the number of pages in a pdf
* picture: for determining the dimension of an image

## Usage
The entrypoint into the tagger is the `object_tagger.tag_file` function.

It expects an `object_tagger.S3ObjectPath(key, bucket)` and a `object_tagger.MetadataHandler(already_tagged, extraction_function, versioning_tag)` object as its parameters.
The parameters of the `MetadataHandler` are as follows:
* `already_tagged`: a function which receives the metadata tags already present on the object, and returns a boolean indicating whether the object should be tagged.
* `extraction_function`: a function receiving the path to the downloaded object, and returning a `string -> string` dictionary embodying the metadata to add to the object
* `versioning_tags`: a `string -> string` dictionary which contains further tags to add to the s3 object, which can for example be used for tag versioning

The function tries to extract the metadata and add it to the object for up to three times.
On success, the added metadata is returned, upon failure an exception is thrown.

For an example, see the service utilizing this library for automatically tagging pdfs uploaded to s3 via aws lambda [in the examples directory](./examples/serverless-triggered).

## Structure
### `object_tagger` 
contains the higher-level orchestration:
* `object_tagger.py` contains all the logic for checking whether the file has already been tagged, downloading it, invoking the metadata script, creating the tag object, and adding it to the s3 resource. 

The metadata scripts are stored in their respective folders

### `pdf_tagger`
The pdf tagger uses [PyPDF2](https://pypdf2.readthedocs.io/en/latest/) to determine the amount of pages in a pdf.
Install with the `[pdf]` extra option.

### `picture_tagger`
Using [Pillow](https://python-pillow.org/), the script gets the `width` and `height` of the passed image.
Install with the `[picture]` extra option.

## Testing
Both `pdf_tagger` and `picture_tagger` come with unittests.
There is also an integration test in `tests/test_object_tagger.py`, which expects
a [localstack](https://github.com/localstack/localstack) instance to run in the background.
Furthermore, the following environment variables need to be set:
```bash
LOCALSTACK_S3_ENDPOINT_URL=http://localhost:4566
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
```