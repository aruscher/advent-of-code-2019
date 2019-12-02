

def run_program(program):
    current_read = 0
    opcode = None
    while opcode != 99:
        opcode = program[current_read]
        if opcode == 99:
            return program
        else:
            arg1_pos = program[current_read+1]
            arg1 = program[arg1_pos]
            arg2_pos = program[current_read+2]
            arg2 = program[arg2_pos]
            output_pos = current_read+3
            if opcode == 1:
                program[output_pos]  = arg1+arg2
            elif opcode == 2:
                program[output_pos]  = arg1*arg2
            current_read+=4



def main():
    program = [int(x) for x in input().split(",")]
    run_program(program)



    print(program)


if __name__ == '__main__':
    main()