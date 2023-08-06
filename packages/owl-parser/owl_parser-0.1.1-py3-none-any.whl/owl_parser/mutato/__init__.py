from .bp import *
from .svc import *
from .dmo import *
from .dto import *


from baseblock import FileIO
from baseblock import Enforcer

from owl_parser.multiquery.bp import FindOntologyData

from owl_parser.mutato.bp import MutatoAPI


def owl_parse(tokens: list,
              ontology_name: str,
              absolute_path: str):

    Enforcer.is_list_of_dicts(tokens)
    Enforcer.is_str(ontology_name)
    FileIO.exists_or_error(absolute_path)

    finder = FindOntologyData(ontologies=[ontology_name],
                              absolute_path=absolute_path)

    api = MutatoAPI(finder)
    svcresult = api.swap(tokens=tokens)

    Enforcer.is_list_of_dicts(svcresult)

    return svcresult
