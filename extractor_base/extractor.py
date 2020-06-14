from typing import IO, Dict, List, Tuple, Any

class Extractor:
    class_alias = ''

    def __init__(self,*args):
        self.__childs:List[Extractor] = list(args)

    def add_childs(self, *args):
        for x in args:
            self.__childs.append(x)

    def leaf(self)->bool:
        return len(self.__childs) == 0

    @property
    def alias(self) -> str:
        return self.class_alias

    def get_info(self, pdf: IO, password:str = None) -> Dict[str, Any]:
        info = {}
        for x in self.__childs:
            info  = self._merge(info, x.get_info(pdf,password))
        return info

    def _merge(self, info1:Dict[str,Any], info2:Dict[str,Any])->Dict[str,Any]:
        result = info1
        for key, value in info2.items():
            if key in result.keys():
                result[key] = self._compare_and_decide(key, result[key], value)
            result[key] = value
        return result

    def _compare_and_decide(self, key, value1, value2):
        return value1

    @property
    def childs(self): return self.__childs

    def  __len__(self):
       l = 1
       for x in self.__childs:
           l += len(x)
       return l