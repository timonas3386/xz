#ifndef XZ_HARNESS_H
#define XZ_HARNESS_H

#include <sys/types.h>
extern char *log_file_name;

void harness_init(void);
void harness_close(void);
ssize_t harness_write(int fd, const void *buf, size_t count);
off_t harness_lseek(int __fd, off_t __offset, int __whence);
#endif