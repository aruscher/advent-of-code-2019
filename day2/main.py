

def execute_program(program, start=0):
    opcode = program[start]
    if opcode == 99:
        return program
    arg1i,arg2i,outi = program[start+1:start+4]
    arg1,arg2 = program[arg1i],program[arg2i]
    result = 0
    if opcode == 1:
        result = arg1+arg2
    elif opcode == 2:
        result = arg1*arg2
    else:
        raise ValueError("Unknown opcode")
    program[outi] = result
    return execute_program(program, start + 4)

def run_program(program,noun=5,verb=2):
    program[1] = noun
    program[2] = verb
    execute_program(program)

def part1(program):
    run_program(program)
    print(f"Result 1: {program[0]}")

def part2(program):
    for noun in range(0,100):
        for verb in range(0,100):
            copy = list(program)
            run_program(copy,noun,verb)
            if copy[0] == 19690720:
                print(f"Result 2: {100*noun+verb}")
                return

def main():
    program = [int(x) for x in input().split(",")]
    part1(list(program))
    part2(list(program))


if __name__ == '__main__':
    main()