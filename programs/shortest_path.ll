; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@.1 = global [3 x i8] c"%d\00"
@.2 = global [20 x i8] c"======OUTPUT======\0A\00"
@.3 = global [4 x i8] c"%d \00"
@.4 = global [2 x i8] c"\0A\00"

; Function Attrs: nounwind
declare noalias i8* @calloc(i32, i32) local_unnamed_addr #0

; Function Attrs: nounwind
declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #0

; Function Attrs: nounwind
declare void @free(i8* nocapture) local_unnamed_addr #0

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
  %.5 = tail call i8* @calloc(i32 %.2, i32 8)
  %.6 = bitcast i8* %.5 to i32**
  %comp43 = icmp eq i32 %.2, 0
  br i1 %comp43, label %end.2.thread, label %cycle

check.2.preheader:                                ; preds = %end.1
  br i1 %comp43, label %end.2.thread, label %check.4.preheader.preheader

cycle:                                            ; preds = %entry, %end.1
  %i.044 = phi i32 [ %.38, %end.1 ], [ 0, %entry ]
  %.14 = tail call i8* @calloc(i32 %.2, i32 4)
  %0 = sext i32 %i.044 to i64
  %.19 = getelementptr i32*, i32** %.6, i64 %0
  %1 = bitcast i32** %.19 to i8**
  store i8* %.14, i8** %1, align 8
  %.31.cast = bitcast i8* %.14 to i32*
  br label %cycle.1

cycle.1:                                          ; preds = %cycle, %cycle.1
  %j.042 = phi i32 [ 0, %cycle ], [ %.35, %cycle.1 ]
  %2 = sext i32 %j.042 to i64
  %.32 = getelementptr i32, i32* %.31.cast, i64 %2
  %.33 = tail call i32 @readint()
  store i32 %.33, i32* %.32, align 4
  %.35 = add nuw i32 %j.042, 1
  %comp.1 = icmp eq i32 %.35, %.2
  br i1 %comp.1, label %end.1, label %cycle.1

end.1:                                            ; preds = %cycle.1
  %.38 = add nuw i32 %i.044, 1
  %comp = icmp eq i32 %.38, %.2
  br i1 %comp, label %check.2.preheader, label %cycle

check.4.preheader.preheader:                      ; preds = %check.2.preheader, %end.3
  %k.012 = phi i32 [ %.109, %end.3 ], [ 0, %check.2.preheader ]
  %3 = sext i32 %k.012 to i64
  %.73 = getelementptr i32*, i32** %.6, i64 %3
  %.74.pre = load i32*, i32** %.73, align 8
  br label %check.4.preheader

check.4.preheader:                                ; preds = %check.4.preheader.preheader, %end.4
  %i.1.09 = phi i32 [ %.106, %end.4 ], [ 0, %check.4.preheader.preheader ]
  %4 = sext i32 %i.1.09 to i64
  %.59 = getelementptr i32*, i32** %.6, i64 %4
  %.60 = load i32*, i32** %.59, align 8
  %.68 = getelementptr i32, i32* %.60, i64 %3
  br label %cycle.4

cycle.4:                                          ; preds = %check.4.preheader, %merge
  %j.1.07 = phi i32 [ 0, %check.4.preheader ], [ %.103, %merge ]
  %5 = sext i32 %j.1.07 to i64
  %.61 = getelementptr i32, i32* %.60, i64 %5
  %.62 = load i32, i32* %.61, align 4
  %.69 = load i32, i32* %.68, align 4
  %.75 = getelementptr i32, i32* %.74.pre, i64 %5
  %.76 = load i32, i32* %.75, align 4
  %.77 = add i32 %.76, %.69
  %.78 = icmp sgt i32 %.62, %.77
  br i1 %.78, label %then, label %merge

then:                                             ; preds = %cycle.4
  store i32 %.77, i32* %.61, align 4
  br label %merge

merge:                                            ; preds = %then, %cycle.4
  %.103 = add nuw i32 %j.1.07, 1
  %comp.4 = icmp eq i32 %.103, %.2
  br i1 %comp.4, label %end.4, label %cycle.4

end.4:                                            ; preds = %merge
  %.106 = add nuw i32 %i.1.09, 1
  %comp.3 = icmp eq i32 %.106, %.2
  br i1 %comp.3, label %end.3, label %check.4.preheader

end.3:                                            ; preds = %end.4
  %.109 = add nuw i32 %k.012, 1
  %comp.2 = icmp eq i32 %.109, %.2
  br i1 %comp.2, label %end.2, label %check.4.preheader.preheader

end.2.thread:                                     ; preds = %check.2.preheader, %entry
  %.11246 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.2, i64 0, i64 0))
  br label %end.5

end.2:                                            ; preds = %end.3
  %.112 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.2, i64 0, i64 0))
  br i1 %comp43, label %end.5, label %check.6.preheader

check.6.preheader:                                ; preds = %end.2, %end.6
  %i.2.05 = phi i32 [ %.141, %end.6 ], [ 0, %end.2 ]
  %6 = sext i32 %i.2.05 to i64
  %.136 = getelementptr i32*, i32** %.6, i64 %6
  %.127 = load i32*, i32** %.136, align 8
  %7 = bitcast i32* %.127 to i8*
  br label %cycle.6

cycle.6:                                          ; preds = %check.6.preheader, %cycle.6
  %j.2.03 = phi i32 [ 0, %check.6.preheader ], [ %.131, %cycle.6 ]
  %8 = sext i32 %j.2.03 to i64
  %.128 = getelementptr i32, i32* %.127, i64 %8
  %.129 = load i32, i32* %.128, align 4
  %.130 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.3, i64 0, i64 0), i32 %.129)
  %.131 = add nuw i32 %j.2.03, 1
  %comp.6 = icmp eq i32 %.131, %.2
  br i1 %comp.6, label %end.6, label %cycle.6

end.6:                                            ; preds = %cycle.6
  tail call void @free(i8* nonnull %7)
  %.140 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.4, i64 0, i64 0))
  %.141 = add nuw i32 %i.2.05, 1
  %comp.5 = icmp eq i32 %.141, %.2
  br i1 %comp.5, label %end.5, label %check.6.preheader

end.5:                                            ; preds = %end.6, %end.2.thread, %end.2
  tail call void @free(i8* %.5)
  ret void
}

attributes #0 = { nounwind }
