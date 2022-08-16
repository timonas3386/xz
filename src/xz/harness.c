#include "harness.h"
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

static unsigned long address;
static FILE *record;
char *log_file_name;

void harness_init(void) {
  if (!log_file_name)
    log_file_name = "harness.csv";
  record = fopen(log_file_name, "w");
  if (!record) {
    fprintf(stderr, "Error: Failed to open file %s in %s", log_file_name,
            __func__);
    exit(EXIT_FAILURE);
  }
}

void harness_close(void) { fclose(record); }

ssize_t harness_write(int fd, const void *buf, size_t count) {
  fprintf(record, "%lu, %lu\n", address, count);
  address += count;
  return count;
}

off_t harness_lseek(int __fd, off_t __offset, int __whence) {
  address += __offset;
  return address;
}