from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
    TimestampType,
)


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class ResearchElementDefinition_CharacteristicSchema:
    """
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
    ) -> Union[StructType, DataType]:
        """
        The ResearchElementDefinition resource describes a "PICO" element that
        knowledge (evidence, assertion, recommendation) is about.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        definitionCodeableConcept: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionCanonical: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionExpression: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionDataRequirement: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        usageContext: Use UsageContext to define the members of the population, such as Age Ranges,
            Genders, Settings.

        exclude: When true, members with this characteristic are excluded from the element.

        unitOfMeasure: Specifies the UCUM unit for the outcome.

        studyEffectiveDescription: A narrative description of the time period the study covers.

        studyEffectiveDateTime: Indicates what effective period the study covers.

        studyEffectivePeriod: Indicates what effective period the study covers.

        studyEffectiveDuration: Indicates what effective period the study covers.

        studyEffectiveTiming: Indicates what effective period the study covers.

        studyEffectiveTimeFromStart: Indicates duration from the study initiation.

        studyEffectiveGroupMeasure: Indicates how elements are aggregated within the study effective period.

        participantEffectiveDescription: A narrative description of the time period the study covers.

        participantEffectiveDateTime: Indicates what effective period the study covers.

        participantEffectivePeriod: Indicates what effective period the study covers.

        participantEffectiveDuration: Indicates what effective period the study covers.

        participantEffectiveTiming: Indicates what effective period the study covers.

        participantEffectiveTimeFromStart: Indicates duration from the participant's study entry.

        participantEffectiveGroupMeasure: Indicates how elements are aggregated within the study effective period.

        """
        if extension_fields is None:
            extension_fields = [
                "valueBoolean",
                "valueCode",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valuePositiveInt",
                "valueString",
                "valueTime",
                "valueUnsignedInt",
                "valueUri",
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.r4.complex_types.expression import ExpressionSchema
        from spark_fhir_schemas.r4.complex_types.datarequirement import (
            DataRequirementSchema,
        )
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContextSchema
        from spark_fhir_schemas.r4.complex_types.period import PeriodSchema
        from spark_fhir_schemas.r4.complex_types.duration import DurationSchema
        from spark_fhir_schemas.r4.complex_types.timing import TimingSchema

        if (
            max_recursion_limit
            and nesting_list.count("ResearchElementDefinition_Characteristic")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ResearchElementDefinition_Characteristic"
        ]
        my_parent_path = (
            parent_path + ".researchelementdefinition_characteristic"
            if parent_path
            else "researchelementdefinition_characteristic"
        )
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField("definitionCanonical", StringType(), True),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionExpression",
                    ExpressionSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionDataRequirement",
                    DataRequirementSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Use UsageContext to define the members of the population, such as Age Ranges,
                # Genders, Settings.
                StructField(
                    "usageContext",
                    ArrayType(
                        UsageContextSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # When true, members with this characteristic are excluded from the element.
                StructField("exclude", BooleanType(), True),
                # Specifies the UCUM unit for the outcome.
                StructField(
                    "unitOfMeasure",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # A narrative description of the time period the study covers.
                StructField("studyEffectiveDescription", StringType(), True),
                # Indicates what effective period the study covers.
                StructField("studyEffectiveDateTime", TimestampType(), True),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectivePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectiveDuration",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectiveTiming",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates duration from the study initiation.
                StructField(
                    "studyEffectiveTimeFromStart",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField("studyEffectiveGroupMeasure", StringType(), True),
                # A narrative description of the time period the study covers.
                StructField("participantEffectiveDescription", StringType(), True),
                # Indicates what effective period the study covers.
                StructField("participantEffectiveDateTime", TimestampType(), True),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectivePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveDuration",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveTiming",
                    TimingSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates duration from the participant's study entry.
                StructField(
                    "participantEffectiveTimeFromStart",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path,
                    ),
                    True,
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField("participantEffectiveGroupMeasure", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                c
                if c.name != "modifierExtension"
                else StructField("modifierExtension", StringType(), True)
                for c in schema.fields
            ]

        return schema
