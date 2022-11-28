zvalid_tld = ['.com', '.net', '.org', '.edu', '.gov', '.mil', '.int', '.io', '.co', '.bd','.ac.bd','.gov.bd','.com.bd',
              '.net.bd','.org.bd','.edu.bd','.mil.bd','.int.bd','.io.bd','.co.bd','.ac.uk','.gov.uk','.uk','.ac.in',
              '.gov.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae',
              '.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw',
              '.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr',
              '.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in',
              '.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il',
              '.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn',
              '.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th',
              '.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.me']
zspecial_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', 
                      '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', '?', '~', 
                      '`', '.', ',', '/', '\\']
# import from input file 
 
def EmailChecker(email):
        if email.count('@') <= 1:
            if email.find('.') != -1:
                if email.startswith('@') == False and email.endswith('@') == False and email.startswith('.') == False and email.endswith('.') == False:
                    # if starts with digit 
                    if email[0].isdigit() == False:
                        if email[0] not in zspecial_characters:
                            if email[-1] not in zspecial_characters:
                                after_at = email[email.find('@'):]
                                if after_at.find('.') != -1:
                                        return True
        else: 
            return False 
def WebAddressChecker(address):
    if address.lower().startswith('www'):
        if address.count('.') >= 2:
            if address[address.find('.')+1:][0] not in zspecial_characters:
                # if any(address.endswith(tld) for tld in zvalid_tld if address.count(tld) == 1):
                    return True
                     
    else:
        return False

if __name__=="__main__":
    with open('Lab-2/input.txt', 'r') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        lines.pop(0)

        for index,line in enumerate(lines):  
            
            if EmailChecker(line):
                print(f"Email, {index+1}")
                
            elif WebAddressChecker(line):
                print(f"Web, {index+1}")
                
            else: 
                print(f"Invalid, {index+1}")
    f.close()
        
        