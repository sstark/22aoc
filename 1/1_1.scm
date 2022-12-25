#!/usr/bin/env gosh
(define (read-elf-2 calories)
  (let1 l (read-line)
    (cond [(eof-object? l)
           (values calories #t)]
          [else
           (if-let1 c (string->number l)
                    (read-elf-2 (+ calories c))
                    (values calories #f))])))

(define (read-elf) (read-elf-2 0))

(define (main args)
  (let ((max-calories -1)
        (max-elf #f))
    (let loop ((elf 1))
      (receive (calories last-elf?)
          (read-elf)
        (when (> calories max-calories)
          (set! max-calories calories)
          (set! max-elf elf))
        (when (not last-elf?)
          (loop (+ elf 1)))))
    (print "elf " max-elf " carries " max-calories " calories"))
  0)
