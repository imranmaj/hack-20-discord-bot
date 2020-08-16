from run_java import run_java


simple_program = 'public static void main(String[] args){System.out.println("Hi");}'
longer_program = 'public static void main(String[] args){for(int i = 0; i < 2000; i++){System.out.println(i);}}'
memory_program = 'public static void main(String[] args){int[] x = new int[1000]; System.out.println(x.length);}'
broken_program = 'public static void main(String[] args){System.out.println("Hello);}'


print(run_java(simple_program))
print(run_java(memory_program))
# print(run_java(broken_program))
print(run_java(longer_program))