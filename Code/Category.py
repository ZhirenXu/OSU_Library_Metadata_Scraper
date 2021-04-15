categoryDict = {"Internal ID Link": "id link",
                "Resource Type": "attribute attribute-resource_type",
                "Title": "Title",
                "Alternative Title": "attribute attribute-alternative",
                "Creator": "attribute attribute-creator",
                "Contributor": "attribute attribute-contributor",
                "Genre": "attribute attribute-work_type",
                "Language": "attribute attribute-language",
                "Publisher": "attribute attribute-publisher",
                "Date Created": "attribute attribute-date_created",
                "Date Issued": "attribute attribute-issued",
                "Date Copyrighted": "attribute attribute-date_copyrighted",
                "Date": "attribute attribute-date",
                "Summary": "attribute attribute-abstract",
                "Description": "attribute attribute-description",
                "Version": "attribute attribute-bibframe_version",
                "Staff Notes": "attribute attribute-staff_notes",
                "Format": "attribute attribute-format",
                "Medium": "attribute attribute-medium",
                "Extent": "attribute attribute-extent",
                "Measurements": "attribute attribute-measurement",
                "Materials": "attribute attribute-material",
                "Repository": "attribute attribute-based_near_label",
                "Collection": "attribute attribute-collection_name",
                "Sub Collection": "attribute attribute-sub_collection",
                "Source": "attribute attribute-source",
                "Provenance": "attribute attribute-provenance",
                "Related Finding Aid": "attribute attribute-related_finding_aid",
                "Related URL": "attribute attribute-related_url",
                "Identifier": "attribute attribute-identifier",
                "Call Number": "attribute attribute-call_number",
                "Collection Identifier": "attribute attribute-collection_identifier",
                "Archival Context": "attribute attribute-archival_unit",
                "Published In": "attribute attribute-bibliographic_citation",
                "Subject": "attribute attribute-subject",
                "Keyword": "attribute attribute-keyword",
                "Place (Topic)": "attribute attribute-spatial",
                "Time period (Topic)": "attribute attribute-temporal",
                "Rights Statement": "attribute attribute-rights_statement",
                "Rights Notes": "attribute attribute-rights_note",
                "Rights Holder": "attribute attribute-rights_holder",
                "License": "attribute attribute-license_cc",
                "Access Rights": "attribute attribute-access_right",
                "Preservation level": "attribute attribute-preservation_level",
                "Preservation level Rationale": "attribute attribute-preservation_level_rationale",
                "Syndicate": "attribute attribute-syndicate",
                "Permanent link": "attribute attribute-handle"
               }
                
##Return a list of category name we want to put in csv file
# @return   categoryList
#           The list contain all category name
def getCategoryList():
    categoryList = categoryDict.keys()
    return categoryList

def getLiTagList():
    liTagList = categoryDict.values()

    return liTagList
