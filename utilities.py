class Utilities:

    @staticmethod
    def str_to_dec(bin_str, length):

        aux = list(bin_str)
        aux2 = length
        dec_num = 0

        for element in aux:
            aux2 -= 1
            # print(aux2)
            if element == '1':
                dec_num += 2**aux2
                # print(2**aux2)

        return dec_num
