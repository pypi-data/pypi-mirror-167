from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CarePlanSchema:
    """
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
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
            "valueQuantity",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        Describes the intention of how one or more practitioners intend to deliver
        care for a particular patient, group or community for a period of time,
        possibly limited to care for a specific condition or set of conditions.
        If the element is present, it must have either a @value, an @id, or extensions


            id: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content may not always be associated with
        version changes to the resource.
            implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content.
            language: The base language in which the resource is written.
            text: A human-readable narrative that contains a summary of the resource, and may be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            extension: May be used to represent additional information that is not part of the basic
        definition of the resource. In order to make the use of extensions safe and
        manageable, there is a strict set of governance  applied to the definition and
        use of extensions. Though any implementer is allowed to define an extension,
        there is a set of requirements that SHALL be met as part of the definition of
        the extension.
            modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource, and that modifies the understanding of the element
        that contains it. Usually modifier elements provide negation or qualification.
        In order to make the use of extensions safe and manageable, there is a strict
        set of governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.
            identifier: This records identifiers associated with this care plan that are defined by
        business processes and/or used to refer to it when a direct URL reference to
        the resource itself is not appropriate (e.g. in CDA documents, or in written /
        printed documentation).
            subject: Identifies the patient or group whose intended care is described by the plan.
            status: Indicates whether the plan is currently being acted upon, represents future
        intentions or is now a historical record.
            context: Identifies the context in which this particular CarePlan is defined.
            period: Indicates when the plan did (or is intended to) come into effect and end.
            author: Identifies the individual(s) or ogranization who is responsible for the
        content of the care plan.
            modified: Identifies the most recent date on which the plan has been revised.
            category: Identifies what "kind" of plan this is to support differentiation between
        multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma",
        "disease management", "wellness plan", etc.
            description: A description of the scope and nature of the plan.
            addresses: Identifies the conditions/problems/concerns/diagnoses/etc. whose management
        and/or mitigation are handled by this plan.
            support: Identifies portions of the patient's record that specifically influenced the
        formation of the plan.  These might include co-morbidities, recent procedures,
        limitations, recent assessments, etc.
            relatedPlan: Identifies CarePlans with some sort of formal relationship to the current
        plan.
            participant: Identifies all people and organizations who are expected to be involved in the
        care envisioned by this plan.
            goal: Describes the intended objective(s) of carrying out the care plan.
            activity: Identifies a planned action to occur as part of the plan.  For example, a
        medication to be used, lab tests to perform, self-monitoring, education, etc.
            note: General notes about the care plan not covered elsewhere.
        """
        # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema

        # meta
        from spark_fhir_schemas.dstu2.complex_types.meta import MetaSchema

        # implicitRules
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema

        # language
        # type = code
        # text
        from spark_fhir_schemas.dstu2.complex_types.narrative import NarrativeSchema

        # contained
        from spark_fhir_schemas.dstu2.complex_types.resourcecontainer import (
            ResourceContainerSchema,
        )

        # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema

        # identifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema

        # subject
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema

        # period
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema

        # modified
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema

        # category
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )

        # relatedPlan
        from spark_fhir_schemas.dstu2.backbone_elements.careplanrelatedplan import (
            CarePlanRelatedPlanSchema,
        )

        # participant
        from spark_fhir_schemas.dstu2.backbone_elements.careplanparticipant import (
            CarePlanParticipantSchema,
        )

        # activity
        from spark_fhir_schemas.dstu2.backbone_elements.careplanactivity import (
            CarePlanActivitySchema,
        )

        # note
        from spark_fhir_schemas.dstu2.complex_types.annotation import AnnotationSchema

        if (
            max_recursion_limit
            and nesting_list.count("CarePlan") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CarePlan"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
                StructField("language", StringType(), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceContainerSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
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
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
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
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # This records identifiers associated with this care plan that are defined by
                # business processes and/or used to refer to it when a direct URL reference to
                # the resource itself is not appropriate (e.g. in CDA documents, or in written /
                # printed documentation).
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies the patient or group whose intended care is described by the plan.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Indicates whether the plan is currently being acted upon, represents future
                # intentions or is now a historical record.
                StructField("status", StringType(), True),
                # Identifies the context in which this particular CarePlan is defined.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Indicates when the plan did (or is intended to) come into effect and end.
                StructField(
                    "period",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Identifies the individual(s) or ogranization who is responsible for the
                # content of the care plan.
                StructField(
                    "author",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies the most recent date on which the plan has been revised.
                StructField(
                    "modified",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Identifies what "kind" of plan this is to support differentiation between
                # multiple co-existing plans; e.g. "Home health", "psychiatric", "asthma",
                # "disease management", "wellness plan", etc.
                StructField(
                    "category",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # A description of the scope and nature of the plan.
                StructField("description", StringType(), True),
                # Identifies the conditions/problems/concerns/diagnoses/etc. whose management
                # and/or mitigation are handled by this plan.
                StructField(
                    "addresses",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies portions of the patient's record that specifically influenced the
                # formation of the plan.  These might include co-morbidities, recent procedures,
                # limitations, recent assessments, etc.
                StructField(
                    "support",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies CarePlans with some sort of formal relationship to the current
                # plan.
                StructField(
                    "relatedPlan",
                    ArrayType(
                        CarePlanRelatedPlanSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies all people and organizations who are expected to be involved in the
                # care envisioned by this plan.
                StructField(
                    "participant",
                    ArrayType(
                        CarePlanParticipantSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Describes the intended objective(s) of carrying out the care plan.
                StructField(
                    "goal",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies a planned action to occur as part of the plan.  For example, a
                # medication to be used, lab tests to perform, self-monitoring, education, etc.
                StructField(
                    "activity",
                    ArrayType(
                        CarePlanActivitySchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # General notes about the care plan not covered elsewhere.
                StructField(
                    "note",
                    AnnotationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        return schema
