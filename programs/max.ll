; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@.1 = global [3 x i8] c"%d\00"
@.2 = global [17 x i8] c"Prilis male N!!!\00"
@.3 = global [16 x i8] c"Maximum je: %d\0A\00"

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
  %.5 = icmp slt i32 %.2, 1
  br i1 %.5, label %then, label %merge

then:                                             ; preds = %entry
  %.7 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([17 x i8], [17 x i8]* @.2, i64 0, i64 0))
  ret void

merge:                                            ; preds = %entry
  %.9 = tail call i32 @readint()
  %.12 = add i32 %.2, -1
  %comp1 = icmp eq i32 %.12, 0
  br i1 %comp1, label %end, label %cycle

cycle:                                            ; preds = %merge, %cycle
  %i.03 = phi i32 [ %.26, %cycle ], [ 0, %merge ]
  %max.02 = phi i32 [ %spec.select, %cycle ], [ %.9, %merge ]
  %.17 = tail call i32 @readint()
  %.21 = icmp sgt i32 %.17, %max.02
  %spec.select = select i1 %.21, i32 %.17, i32 %max.02
  %.26 = add nuw i32 %i.03, 1
  %comp = icmp eq i32 %.26, %.12
  br i1 %comp, label %end, label %cycle

end:                                              ; preds = %cycle, %merge
  %max.0.lcssa = phi i32 [ %.9, %merge ], [ %spec.select, %cycle ]
  %.30 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.3, i64 0, i64 0), i32 %max.0.lcssa)
  ret void
}

attributes #0 = { nounwind }
