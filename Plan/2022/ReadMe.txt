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
    
    
寄存器:
    CR1 : 未定义的控制寄存器，供将来的处理器使用
    CR2 : 页故障线性地址寄存器, 保存最后一次出现页故障的全32位线性地址
    CR3 : 页目录基址寄存器，保存页目录表的物理地址，页目录表总是放在以4K字节为单位的存储器边界上，因此，它的地址的低12位总为0，不起作用，即使写上内容，也不会被理会
    
    sp/esp/rsp : 栈寄存器---指向栈顶
    bp/ebp/rbp : 栈基址寄存器---指向栈底
    ip/eip/rip : 程序指令寄存器---指向下一条待执行指令
