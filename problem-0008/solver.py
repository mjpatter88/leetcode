class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()
        if not str:
            return 0
        if not (str[0].isdigit() or str[0] == '-' or str[0] == '+'):
            return 0

        new_str = []
        if str[0] == '-':
            new_str.append('-')
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        for char in str:
            if not char.isdigit():
                break
            new_str.append(char)

        try:
            answer = int("".join(new_str))
        except Exception as e:
            answer = 0
        if answer < -(2**31):
            return -(2**31)
        elif answer > 2**31 -1:
            return 2**31 -1
        else:
            return answer
