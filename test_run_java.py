from run_java import run_java


simple_program = 'public static void main(String[] args){System.out.println("Hi");}'
broken_program = 'public static void main(String[] args){System.out.println("Hello);}'


print("This should work")
print(run_java(simple_program))
print("This should break")
print(run_java(broken_program))
