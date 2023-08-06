# json提取器
import random

from tool import log
import jsonpath

def json_excutor(send_request,var_name,index,*json_path):
    json_path=",".join(json_path)
    if not hasattr(send_request,'response'):
        log.erro(f"$__JSON_EXCUTOR({index},{jsonpath})$关键字只能用于后置或者断言中")
        return
    response=None
    try:
        response=send_request.response.res_json
    except:
        log.erro(f"$__JSON_EXCUTOR({index},{jsonpath})$关键字只能用于json格式")
        raise
    json_path = json_path.replace('"', "'")
    res_list=jsonpath.jsonpath(response,json_path)
    if res_list:
        index=int(index)
        if index>0:
            res=res_list[index-1]
        else:
            res=random.choice(res_list)

        send_request.dict_var[var_name]=res
        # log.debug(f"变量值{var_name}:{res}")


def get_var(send_request,var_name):       #取变量
    vars=send_request.dict_var
    if var_name in vars:
        return vars[var_name]



def set_var(send_request,var_name,value):   #存变量
    send_request.dict_var[var_name]=value





def assert_contains(send_request,*hope):          #包含断言
    hope=",".join(hope)
    if not hasattr(send_request,'response'):
        log.erro(f"$__assert_contains{hope}关键字，只能用于back或assert当中")
        return
    body_text=send_request.response.res_text
    try:
        assert hope in body_text
    except:
        log.erro(f"断言失败，响应正文中不包含：{hope}")
        raise



def assert_json(send_request,hope,*json_path):    #json断言
    json_path=",".join(json_path)
    if not hasattr(send_request,'response'):
        log.erro(f"$__assert_contains{hope}关键字，只能用于back或assert当中")
        return
    response=None
    try:
        response=send_request.response.res_json
    except:
        log.erro(f"$__assert_json{hope},{json_path}$关键字，只能用于响应数据为json格式")
        raise
    json_path=json_path.replace('"',"'")
    res=jsonpath.jsonpath(response,json_path)
    log.debug(json_path)
    try:
        if res :
            if hope.isdigit():
                assert res[0]==int(hope)
            else:
                assert res[0]==hope
        else:
            assert False
    except:
        log.erro(f"断言失败，json_path:{json_path}对应数据{res}不存在，或与预期结果不一致")
        raise


