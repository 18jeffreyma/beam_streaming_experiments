
from __future__ import absolute_import

import argparse
import logging

from past.builtins import unicode

import apache_beam as beam

from apache_beam import window
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.transforms.trigger import AfterCount
from apache_beam.transforms.trigger import AccumulationMode
from apache_beam.io import fileio

def run(argv=None, save_main_session=True):
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input_topic',
      required=True,
      help=(
          'Input PubSub topic of the form '
          '"projects/<PROJECT>/topics/<TOPIC>".'))
  known_args, pipeline_args = parser.parse_known_args(argv)

  parser.add_argument(
      '--output_dir',
      required=True,
      help=(
          'Output directory to write to.'))
  known_args, pipeline_args = parser.parse_known_args(argv)

  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
  pipeline_options.view_as(StandardOptions).streaming = True

  with beam.Pipeline(options=pipeline_options) as p:
    messages = (p | beam.io.ReadFromPubSub(topic=known_args.input_topic).with_output_types(bytes))

    lines = (messages | 'decode' >> beam.Map(lambda x: x.decode('utf-8')).with_output_types(unicode))

    # do stuff here

    windowed = (lines | beam.WindowInto(window.GlobalWindows(),
                trigger=AfterCount(1),
                accumulation_mode=AccumulationMode.DISCARDING))

    windowed | 'write' >> fileio.WriteToFiles(path=known_args.output_dir)

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()

