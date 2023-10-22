
class StrHelper:
    
    def money_mask(self, number):
        return "${:,.0f}".format(int(number)).replace(',', '.')
        
str_helper_singleton = StrHelper()