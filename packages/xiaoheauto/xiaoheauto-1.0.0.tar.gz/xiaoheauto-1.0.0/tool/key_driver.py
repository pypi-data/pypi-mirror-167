import json
import re

from tool.key_map import key_mps


class KeyDriver():
    def __init__(self,send_request,value):
        self.send_request=send_request
        self.value=self.to_str(value)
        self.key_replace()



    def to_str(self,value):
        if isinstance(value,dict) or isinstance(value,list):
            value=json.dumps(value,ensure_ascii=False)
        else:
            value=str(value)
        return value



    def paser(self,value):
        '''
        返回字符串中的所有关键字
        $__PHONE()$
        $__RANDOM_STR(abcdefg,10)$
        $__RANDOM_INT$(6,10)$
        $__RANDOM_STR(abcdefg,$__RANDOM_INT$(6,10)$)$
        :return:
        '''
        star=-1
        flag=0
        lenth=len(value)
        keys=[]
        for key in range(lenth):
            if value[key]=='$':
                if key+2<lenth and value[key:key+3]=='$__':
                    # print(f'{key}起始关键字')
                    flag-=1
                    if star<0:
                        star=key
                elif key - 1>0 and value[key-1 : key+1]==")$":
                    # print(f'{key}为结束字符')
                    flag+=1
                    if flag==0:
                        # print(value[star:key+1])
                        keys.append(value[star:key+1])
                        star=-1
        return keys


    def key_run(self,key):
        if "$__" in key[3:-1]:
            in_keys = self.paser(key[3:-1])
            for i_key in in_keys:
                res=self.key_run(i_key)
                key=key.replace(i_key,res)
        key_name=key[3:key.find("(")]
        r=re.compile(r"\((.*?)\)")
        key_args=r.findall(key)[0]
        if key_args=="":
            res=key_mps[key_name](self.send_request)
        else:
            res=key_mps[key_name](self.send_request,*key_args.split(","))
        return self.to_str(res) if res else None


    def key_replace(self):
        keys=self.paser(self.value)
        for key in keys:
            res=self.key_run(key)
            if res:
                self.value = self.value.replace(key, self.to_str(res))
        return self.value


    def __str__(self):
        return self.value





