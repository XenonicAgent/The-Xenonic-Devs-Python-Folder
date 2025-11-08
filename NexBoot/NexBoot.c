// NexBoot kernel (16-bit Real Mode)
// Compile with i686-elf-gcc -ffresstanding -m16 -c NexBoot.c -o kernel.o
// Link with: i686-elf-id -T Linker.ld kernel.o -o kernel.bin

// VGA text mode base address
#define VGA_BUFFER 0xB8000
#define VGA_WIDTH 80
#define VGA_HEIGHT 25

// Write a character to VGA buffer with color 
void vga_put_char(int x, int y, char c, unsigned char color) {
    unsigned short*vga = (unsigned short*)VGA_BUFFER;
    vga[y * VGA_WIDTH + x] = (color << 8) | c;
}

// Clear VGA Screen
void vga_clear(unsigned char bg_color) {
    unsigned short*vga = (unsigned short*)VGA_BUFFER;
    for (int i = 0; i < VGA_WIDTH * VGA_HEIGHT; i++) {
        vga[i] = (bg_color << 8) | ' ';
    }
}

// Print string at position with color 
void vga_print(int x, int y, const char* str, unsigned char color) {
    unsigned short* vga = (unsigned short*)VGA_BUFFER;
    int i = 0;
    while (str[i]) {
        vga[y * VGA_WIDTH + x + i] = (color << 8) | str[i];
        i++;
    }
}

// Kernel entry point 
void kernel_main() {
    // Clear screen (black background, 0x0)
    vga_clear(0x0)

    // Print welcome message (white text on blue background, 0x1F)
    vga_print(10, 10 "Welcome to NexBoot", 0x1F);

    // Infinite loop
    while (1) {
        asm volatile ("hlt");
    }
}
