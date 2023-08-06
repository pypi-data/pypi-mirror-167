from .singlequery import *
from .multiquery import *
from .mutato import *


from baseblock import FileIO
from baseblock import Enforcer


def owl_parser(tokens: list,
               ontology_name: str,
               absolute_path: str) -> list:

    Enforcer.is_list_of_dicts(tokens)
    Enforcer.is_str(ontology_name)
    FileIO.exists_or_error(absolute_path)

    from owl_parser.multiquery.bp import FindOntologyData
    from owl_parser.mutato.bp import MutatoAPI

    finder = FindOntologyData(ontologies=[ontology_name],
                              absolute_path=absolute_path)

    results = MutatoAPI(finder).swap(tokens)
    Enforcer.is_list_of_dicts(results)

    return results
