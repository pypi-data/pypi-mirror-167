# Custom functions <!-- omit in toc -->

## Table of contents <!-- omit in toc -->

1. [Utility](#utility)
   1. [Hash file](#hash-file)
   2. [Hash string](#hash-string)

## Utility

### Hash file

```sh
rotom hash-file [target_file]
```

Supported options included:

- algo: Type of hash algorithm [Default: md5]
- length: Length of final output, truncated by shake_256, < 0 for full hash

---

### Hash string

```sh
rotom hash-str [input_str]
```

Supported options included:

- algo: Type of hash algorithm [Default: md5]
- length: Length of final output, truncated by shake_256, < 0 for full hash

---
