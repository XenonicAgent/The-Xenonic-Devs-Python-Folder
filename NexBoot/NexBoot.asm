BITS 16
ORG 0x7C00

start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7C00

    ; Reset disk
    mov ah, 0
    int 0x13

    ; Load kerenel from sector 2 (after bootloader)
    mov bx, 0x1000 ; Load address
    mov ah, 2      ; Read sectors
    mov al, 8      ; Numbers of sectors (adjust as needed)
    mov ch, 0      ; Cylinder
    mov cl, 2      ; Sector
    mov dh         ; Head
    int 0x13
    jc error

    ; Switch to protector mode 
    lgdt [gdt_descriptor]
    mov eax, cr0
    or al, 1
    mov cr0, eax

    jmp 0x08:protected_mode ; Far jump to flush pipeline

error:
    mov si, err_msg
    call print_string
    hlt

print_string:
    mov ah, 0x0E
    lodsb
    test al, al
    jz .done
    int 0x10
    jmp print_string
.done:
    ret

error.msg: db "Disk error !", 0

gdt_start:
    dq 0  ; Null descriptor
    dd 0x0000FFFF, 0X00CF9A00 ; Code segment
    dd 0x0000FFFF, 0X00CF9200 ; Data segment

gdt_descriptor:
    dw gdt_descriptor - gdt_start - 1
    dd gdt_start