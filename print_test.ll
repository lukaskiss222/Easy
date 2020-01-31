; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@.1 = global [3 x i8] c"%d\00"
@.2 = global [27 x i8] c"Ide my aj foorloop :D, %d\0A\00"
@.3 = global [4 x i8] c"%d\0A\00"
@.4 = global [3 x i8] c"%s\00"

; Function Attrs: nounwind
declare noalias i8* @calloc(i32, i32) local_unnamed_addr #0

; Function Attrs: nounwind
declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #0

; Function Attrs: nounwind
declare i32 @scanf(i8* nocapture readonly, ...) local_unnamed_addr #0

; Function Attrs: nounwind
define i32 @readint() local_unnamed_addr #0 {
entry:
  %i = alloca i32, align 4
  %.2 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.1, i64 0, i64 0), i32* nonnull %i)
  %.3 = load i32, i32* %i, align 4
  ret i32 %.3
}

; Function Attrs: nounwind
define void @main() local_unnamed_addr #0 {
entry:
  %.2 = tail call i32 @readint()
  %comp1 = icmp eq i32 %.2, 0
  br i1 %comp1, label %end, label %cycle

cycle:                                            ; preds = %entry, %cycle
  %g.02 = phi i32 [ %.12, %cycle ], [ %.2, %entry ]
  %.11 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([27 x i8], [27 x i8]* @.2, i64 0, i64 0), i32 %g.02)
  %.12 = add i32 %g.02, -1
  %comp = icmp eq i32 %.12, 0
  br i1 %comp, label %end, label %cycle

end:                                              ; preds = %cycle, %entry
  %.16 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.3, i64 0, i64 0), i32 %.2)
  %.17 = tail call i8* @calloc(i32 100, i32 1)
  %.20 = tail call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.4, i64 0, i64 0), i8* %.17)
  %.22 = tail call i32 (i8*, ...) @printf(i8* %.17)
  ret void
}

attributes #0 = { nounwind }
