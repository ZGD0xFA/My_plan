获取 cpu 使用顺序调用堆栈:
    1. perf record -a -e cycles -o cycle.perf -g sleep 10
    2. perf report -i cycle.perf | more

火焰图:
    1. 预备环境:
        1.1 apt install linux-tools-5.4.0-90-generic -y
        1.2 git clone https://github.com/brendangregg/FlameGraph.git
        
    2. 执行操作:
        2.1 perf record -p 1307430 -F 99 -g -- sleep 10            // general perf file
        2.2 perf script -i perf.data > perf.unfold
        2.3 ./stackcollapse-perf.pl perf.unfold >perf.folded
        2.4 ./flamegraph.pl perf.folded >perf.svg
        
linux 补充知识:
    /proc/kallsyms      # linux 下内核符号表