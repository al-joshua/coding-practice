'''John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone
number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and
the address.

Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with
non-alpha-numeric characters (except inside phone number and name).

Examples of John's phone book lines:

"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"

" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"

Could you help John with a program that, given the lines of his phone book and a phone number returns a string for this
 number : "Phone => num, Name => name, Address => adress"

Examples:

s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
It can happen that, for a few phone numbers, there are many people for a phone number -say nb- , then

return : "Error => Too many people: nb"

or it can happen that the number nb is not in the phone book, in that case

return: "Error => Not found: nb"

You can see other examples in the test cases.

JavaScript random tests completed by @matt c

Note

Codewars stdout doesn't print part of a string when between < and >'''


import re


def phone(strng, num):
    def regexer(exp, line):
        reg = re.search(exp, line)
        p = reg.group(0)
        return p, line[:reg.start()] + line[reg.end():]

    if strng.count(num) > 1:
        return "Error => Too many people: {}".format(num)

    if num not in strng:
        return "Error => Not found: {}".format(num)

    for line in strng.splitlines():
        if num in line:
            num, line = regexer('[\d]{1,2}-([\d]{3}-){2}[\d]{4}', line)
            name, line = regexer('<.*>', line)
            address = ' '.join(i for i in re.split('[ ?!*$/+;:_,]', line) if i)
            return "Phone => {}, Name => {}, Address => {}".format(num, name.strip('<>'), address)
