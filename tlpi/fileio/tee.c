#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int num_write, num_read, output_fd;
    int stdin_fd = 0;
    int stdout_fd = 1;
    int buf_size = 16;
    char buf[buf_size];

    output_fd = open(argv[1], O_WRONLY | O_CREAT, S_IRWXU | S_IRWXG | S_IRWXO);

    if (output_fd == -1) {
        exit(1);
    }

    num_write = 0;
    num_read = read(stdin_fd, buf, buf_size);

    while (num_read > 0) {
        num_write = write(stdout_fd, buf, num_read);
        if (num_write != num_read) {
            exit(1);
        }
        num_write = write(output_fd, buf, num_read);
        if (num_write != num_read) {
            exit(1);
        }
        num_read = read(stdin_fd, buf, buf_size);
    }

    exit(0);
}
