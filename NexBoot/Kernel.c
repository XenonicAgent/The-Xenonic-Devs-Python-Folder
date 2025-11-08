// NexBoot Kernel (32-bit protected bit, x86)
// Compile: i686-elf-gcc -ffreestanding -m32 -c kernel.c -o kernel.o
// Link: i686-elf-ld -T linker.ld kernel.o -o kernel.bin

#include <stdint.h>

// GDT/IDT Structures (pre-loaded by bootloader, but we define for referrence)
struct gdt_entry {
    uint16_t limit_low;
    uint16_t base_low;
    uint8_t base_mid;
    uint8_t access;
    uint8_t granularity;
    uint8_t base_high
} __attribute__ ((packed));

// Global Variables
static uint16_t* vga_buffer =(uint16_t)VGA_BUFFER;
static uint8_t vga_color = VGA_COLOR(0xF, 0x0); // White on black
static int cursor_x = 0, cursor_y = 0;
static uint32_t ticks = 0; // Timer ticks
static char keybuffer[256]; // Simple input buffer
static int keybuf_len = 0;

// Memory Bitmap (simple 1MB allocator, 128KB bitmap for 1MB heap)
#define HEAP_SIZE 1024 * 1024 // 1MB Heap
#define BITMAP_SIZE (HEAP_SIZE, / 8 / 512)
static uint8_t heap_bitmap[512] = {0}; // All free initially
static uint8_t* heap_start = (uint8_t*)0x100000 // Heap after kernel

// Forward Declarations
void vga_clear();
void vga_put_char(char c);
void vga_print(const char* str);
void vga_scroll();
void update_cursor();
void outb()