from tool import log


class BaseResponse():
    def __init__(self,response):
        self.response=response
        self.print_log()

    @property
    def status_code(self):
        return self.response.status_code


    @property
    def res_text(self):
        return self.response.text



    @property
    def res_json(self):
        return self.response.json()


    def print_log(self):
        log.info(f"""---------------------响应报文--------------------------
{self.status_code}
{self.res_text}""")


