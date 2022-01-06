# def do_function(var_name: var_type) -> return_type:
#     pass
# def type_hint_example(name: str) -> str:
#     return f"Hello, {name}"


# <Type hints의 장점>
# 1. 사용자에게 인터페이스를 명확히 알려줄 수 있다.
# 2. 함수의 문서화시 parameter에 대한 정보를 명확히 알 수 있다.
# 3. mypy 또는 IDE, linter 등을 통해 코드의 발생 가능한 오류를 사전에 확인 
# 4. 시스템 전체적인 안정성을 확보할 수 있다.


# ex) 파이토치 
# def insert(self, index: int, module: Module) -> None:
# 위 코드의 뜻은 index의 타입은 int고 리턴값은 없구나(None)라는 것을 알 수 있다.