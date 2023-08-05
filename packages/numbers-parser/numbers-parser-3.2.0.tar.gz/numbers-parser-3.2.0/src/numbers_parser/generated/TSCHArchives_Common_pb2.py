# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSCHArchives_Common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import numbers_parser.generated.TSPMessages_pb2 as TSPMessages__pb2
import numbers_parser.generated.TSKArchives_pb2 as TSKArchives__pb2
import numbers_parser.generated.TSDArchives_pb2 as TSDArchives__pb2
import numbers_parser.generated.TSSArchives_pb2 as TSSArchives__pb2
import numbers_parser.generated.TSCH3DArchives_pb2 as TSCH3DArchives__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19TSCHArchives_Common.proto\x12\x04TSCH\x1a\x11TSPMessages.proto\x1a\x11TSKArchives.proto\x1a\x11TSDArchives.proto\x1a\x11TSSArchives.proto\x1a\x14TSCH3DArchives.proto\"B\n\x0bRectArchive\x12\x1a\n\x06origin\x18\x01 \x02(\x0b\x32\n.TSP.Point\x12\x17\n\x04size\x18\x02 \x02(\x0b\x32\t.TSP.Size\"5\n\x1b\x43hartsNSNumberDoubleArchive\x12\x16\n\x0enumber_archive\x18\x01 \x01(\x01\"7\n$ChartsNSArrayOfNSNumberDoubleArchive\x12\x0f\n\x07numbers\x18\x01 \x03(\x01\"\xd0\x01\n\x1c\x44\x45PRECATEDChart3DFillArchive\x12\x1e\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x10.TSD.FillArchive\x12\x38\n\rlightingmodel\x18\x02 \x01(\x0b\x32!.TSCH.Chart3DLightingModelArchive\x12\x15\n\rtextureset_id\x18\x03 \x01(\t\x12)\n\tfill_type\x18\x04 \x01(\x0e\x32\x16.TSCH.FillPropertyType\x12\x14\n\x0cseries_index\x18\x05 \x01(\r\"@\n\x11\x43hartStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"C\n\x14\x43hartNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"A\n\x12LegendStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"D\n\x15LegendNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"D\n\x15\x43hartAxisStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"G\n\x18\x43hartAxisNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"F\n\x17\x43hartSeriesStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"I\n\x1a\x43hartSeriesNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"f\n\tGridValue\x12\x15\n\rnumeric_value\x18\x01 \x01(\x01\x12\x16\n\x0e\x64\x61te_value_1_0\x18\x02 \x01(\x01\x12\x16\n\x0e\x64uration_value\x18\x03 \x01(\x01\x12\x12\n\ndate_value\x18\x04 \x01(\x01\")\n\x07GridRow\x12\x1e\n\x05value\x18\x01 \x03(\x0b\x32\x0f.TSCH.GridValue\"H\n\x19ReferenceLineStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"K\n\x1cReferenceLineNonStyleArchive\x12 \n\x05super\x18\x01 \x01(\x0b\x32\x11.TSS.StyleArchive*\t\x08\x90N\x10\x80\x80\x80\x80\x02*\xbc\x05\n\tChartType\x12\x16\n\x12undefinedChartType\x10\x00\x12\x15\n\x11\x63olumnChartType2D\x10\x01\x12\x12\n\x0e\x62\x61rChartType2D\x10\x02\x12\x13\n\x0flineChartType2D\x10\x03\x12\x13\n\x0f\x61reaChartType2D\x10\x04\x12\x12\n\x0epieChartType2D\x10\x05\x12\x1c\n\x18stackedColumnChartType2D\x10\x06\x12\x19\n\x15stackedBarChartType2D\x10\x07\x12\x1a\n\x16stackedAreaChartType2D\x10\x08\x12\x16\n\x12scatterChartType2D\x10\t\x12\x14\n\x10mixedChartType2D\x10\n\x12\x16\n\x12twoAxisChartType2D\x10\x0b\x12\x15\n\x11\x63olumnChartType3D\x10\x0c\x12\x12\n\x0e\x62\x61rChartType3D\x10\r\x12\x13\n\x0flineChartType3D\x10\x0e\x12\x13\n\x0f\x61reaChartType3D\x10\x0f\x12\x12\n\x0epieChartType3D\x10\x10\x12\x1c\n\x18stackedColumnChartType3D\x10\x11\x12\x19\n\x15stackedBarChartType3D\x10\x12\x12\x1a\n\x16stackedAreaChartType3D\x10\x13\x12\x1e\n\x1amultiDataColumnChartType2D\x10\x14\x12\x1b\n\x17multiDataBarChartType2D\x10\x15\x12\x15\n\x11\x62ubbleChartType2D\x10\x16\x12\x1f\n\x1bmultiDataScatterChartType2D\x10\x17\x12\x1e\n\x1amultiDataBubbleChartType2D\x10\x18\x12\x14\n\x10\x64onutChartType2D\x10\x19\x12\x14\n\x10\x64onutChartType3D\x10\x1a\x12\x14\n\x10radarChartType2D\x10\x1b*\xa1\x01\n\x08\x41xisType\x12\x15\n\x11\x61xis_type_unknown\x10\x00\x12\x0f\n\x0b\x61xis_type_x\x10\x01\x12\x0f\n\x0b\x61xis_type_y\x10\x02\x12\x11\n\raxis_type_pie\x10\x03\x12\x12\n\x0e\x61xis_type_size\x10\x04\x12\x1a\n\x16\x61xis_type_polar_radius\x10\x05\x12\x19\n\x15\x61xis_type_polar_angle\x10\x06*g\n\rScatterFormat\x12\x1a\n\x16scatter_format_unknown\x10\x00\x12\x1d\n\x19scatter_format_separate_x\x10\x01\x12\x1b\n\x17scatter_format_shared_x\x10\x02*l\n\x0fSeriesDirection\x12\x1c\n\x18series_direction_unknown\x10\x00\x12\x1b\n\x17series_direction_by_row\x10\x01\x12\x1e\n\x1aseries_direction_by_column\x10\x02*\xe3\x01\n\x0fNumberValueType\x12\x1a\n\x16numberValueTypeDecimal\x10\x00\x12\x1b\n\x17numberValueTypeCurrency\x10\x01\x12\x1d\n\x19numberValueTypePercentage\x10\x02\x12\x1d\n\x19numberValueTypeScientific\x10\x03\x12\x1b\n\x17numberValueTypeFraction\x10\x04\x12\x17\n\x13numberValueTypeBase\x10\x05\x12#\n\x16numberValueTypeUnknown\x10\x99\xf8\xff\xff\xff\xff\xff\xff\xff\x01*\xba\x01\n\x13NegativeNumberStyle\x12\x1c\n\x18negativeNumberStyleMinus\x10\x00\x12\x1a\n\x16negativeNumberStyleRed\x10\x01\x12\"\n\x1enegativeNumberStyleParentheses\x10\x02\x12(\n$negativeNumberStyleRedAndParentheses\x10\x03\x12\x1b\n\x17negativeNumberStyleNone\x10\x04*\xeb\x02\n\x10\x46ractionAccuracy\x12\x1f\n\x1b\x66ractionAccuracyConflicting\x10\x00\x12)\n\x1c\x66ractionAccuracyUpToOneDigit\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12*\n\x1d\x66ractionAccuracyUpToTwoDigits\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12,\n\x1f\x66ractionAccuracyUpToThreeDigits\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\x16\x66ractionAccuracyHalves\x10\x02\x12\x1c\n\x18\x66ractionAccuracyQuarters\x10\x04\x12\x1b\n\x17\x66ractionAccuracyEighths\x10\x08\x12\x1e\n\x1a\x66ractionAccuracySixteenths\x10\x10\x12\x1a\n\x16\x66ractionAccuracyTenths\x10\n\x12\x1e\n\x1a\x66ractionAccuracyHundredths\x10\x64')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TSCHArchives_Common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHARTTYPE._serialized_start=1385
  _CHARTTYPE._serialized_end=2085
  _AXISTYPE._serialized_start=2088
  _AXISTYPE._serialized_end=2249
  _SCATTERFORMAT._serialized_start=2251
  _SCATTERFORMAT._serialized_end=2354
  _SERIESDIRECTION._serialized_start=2356
  _SERIESDIRECTION._serialized_end=2464
  _NUMBERVALUETYPE._serialized_start=2467
  _NUMBERVALUETYPE._serialized_end=2694
  _NEGATIVENUMBERSTYLE._serialized_start=2697
  _NEGATIVENUMBERSTYLE._serialized_end=2883
  _FRACTIONACCURACY._serialized_start=2886
  _FRACTIONACCURACY._serialized_end=3249
  _RECTARCHIVE._serialized_start=133
  _RECTARCHIVE._serialized_end=199
  _CHARTSNSNUMBERDOUBLEARCHIVE._serialized_start=201
  _CHARTSNSNUMBERDOUBLEARCHIVE._serialized_end=254
  _CHARTSNSARRAYOFNSNUMBERDOUBLEARCHIVE._serialized_start=256
  _CHARTSNSARRAYOFNSNUMBERDOUBLEARCHIVE._serialized_end=311
  _DEPRECATEDCHART3DFILLARCHIVE._serialized_start=314
  _DEPRECATEDCHART3DFILLARCHIVE._serialized_end=522
  _CHARTSTYLEARCHIVE._serialized_start=524
  _CHARTSTYLEARCHIVE._serialized_end=588
  _CHARTNONSTYLEARCHIVE._serialized_start=590
  _CHARTNONSTYLEARCHIVE._serialized_end=657
  _LEGENDSTYLEARCHIVE._serialized_start=659
  _LEGENDSTYLEARCHIVE._serialized_end=724
  _LEGENDNONSTYLEARCHIVE._serialized_start=726
  _LEGENDNONSTYLEARCHIVE._serialized_end=794
  _CHARTAXISSTYLEARCHIVE._serialized_start=796
  _CHARTAXISSTYLEARCHIVE._serialized_end=864
  _CHARTAXISNONSTYLEARCHIVE._serialized_start=866
  _CHARTAXISNONSTYLEARCHIVE._serialized_end=937
  _CHARTSERIESSTYLEARCHIVE._serialized_start=939
  _CHARTSERIESSTYLEARCHIVE._serialized_end=1009
  _CHARTSERIESNONSTYLEARCHIVE._serialized_start=1011
  _CHARTSERIESNONSTYLEARCHIVE._serialized_end=1084
  _GRIDVALUE._serialized_start=1086
  _GRIDVALUE._serialized_end=1188
  _GRIDROW._serialized_start=1190
  _GRIDROW._serialized_end=1231
  _REFERENCELINESTYLEARCHIVE._serialized_start=1233
  _REFERENCELINESTYLEARCHIVE._serialized_end=1305
  _REFERENCELINENONSTYLEARCHIVE._serialized_start=1307
  _REFERENCELINENONSTYLEARCHIVE._serialized_end=1382
# @@protoc_insertion_point(module_scope)
