import subprocess
import shutil
import os
import threading

batch_dir = "./batch_spoilers"
if os.path.exists(batch_dir):
    shutil.rmtree(batch_dir)
os.mkdir(batch_dir)

def genSeed(index):
    subprocess.run(["python", "./cli.py", "--settings_string", "bKEGiRqzxNXnerKEDRAejpFjAIbiDLWIQXr5/ANnj4YTRzu6leyszOKbOrYvhTgfVA4IhkQlS2Nc+EaePxGj12ly+IU5Ym04IUBR6QJE0Z4q+ApBbqevwJIBk0UJooZBdZLLBQF0AIMBOoCBwN2AYQCO4ECQV4AoUDPIGCwd6A4YEKENQHtkKRKitZyJTqZcklmi3gRwdItIuCn6KiLAImIoAr1rjkbtV/vsigcxYigDNZsyqMSRYAExgAExoADxwADx4ACyAACyIAByQAByYABygABqcuUOS4VOmEJIIvoE5IMMJUzG0xg4tC0rlgVocthoTiwVGAmDAjKY4p5FJkRqUAVQCXAwwpMJwhCAkKCw2lIisPEBEjLBMUFSQtFxgZJS4bHB0mLx8gISco", "--output", f"./batch_spoilers/seed{index}.z64", "--batch", "True"])

THREAD_COUNT = 16

seed_gen_count = 10000
batches = int(seed_gen_count / THREAD_COUNT)
for batch in range(batches):
    batch_threads = []
    for subbatch in range(THREAD_COUNT):
        x = (THREAD_COUNT * batch) + subbatch
        batch_threads.append(threading.Thread(target=genSeed, args=(x,)))
    init_batch = THREAD_COUNT * batch
    print(f"[CONSOLE] Generating seeds {init_batch}-{init_batch + THREAD_COUNT}")
    for b in batch_threads:
        b.start()
    for b in batch_threads:
        b.join()

# python .\cli.py --settings_string "bKEGiRqzxNXnerKEDRAejpFjAIbiDLWIQXr5/ANnj4YTRzu6leyszOKbOrYvhTgfVA4IhkQlS2Nc+EaePxGj12ly+IU5Ym04IUBR6QJE0Z4q+ApBbqevwJIBk0UJooZBdZLLBQF0AIMBOoCBwN2AYQCO4ECQV4AoUDPIGCwd6A4YEKENQHtkKRKitZyJTqZcklmi3gRwdItIuCn6KiLAImIoAr1rjkbtV/vsigcxYigDNZsyqMSRYAExgAExoADxwADx4ACyAACyIAByQAByYABygABqcuUOS4VOmEJIIvoE5IMMJUzG0xg4tC0rlgVocthoTiwVGAmDAjKY4p5FJkRqUAVQCXAwwpMJwhCAkKCw2lIisPEBEjLBMUFSQtFxgZJS4bHB0mLx8gISco"  --output "dk64r-seed.z64"