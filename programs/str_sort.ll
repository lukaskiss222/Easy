; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-unknown-linux-gnu"

@.1 = global [3 x i8] c"%d\00"
@.2 = global [2 x i8] c"[\00"
@.3 = global [5 x i8] c"%s, \00"
@.4 = global [3 x i8] c"]\0A\00"
@.5 = global [3 x i8] c"%s\00"
@.6 = global [10 x i8] c"Sorting: \00"
@.7 = global [43 x i8] c"===========SORTED OUTPUT=================\0A\00"

; Function Attrs: nounwind
declare noalias i8* @calloc(i32, i32) local_unnamed_addr #0

; Function Attrs: nounwind
declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #0

; Function Attrs: nounwind
declare void @free(i8* nocapture) local_unnamed_addr #0

; Function Attrs: nounwind
declare i32 @scanf(i8* nocapture readonly, ...) local_unnamed_addr #0

; Function Attrs: nounwind readonly
declare i32 @strcmp(i8* nocapture, i8* nocapture) local_unnamed_addr #1

; Function Attrs: nounwind
define i32 @readint() local_unnamed_addr #0 {
entry:
  %i = alloca i32, align 4
  %.2 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.1, i64 0, i64 0), i32* nonnull %i)
  %.3 = load i32, i32* %i, align 4
  ret i32 %.3
}

; Function Attrs: nounwind
define void @printarr(i8** nocapture readonly %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %.6 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.2, i64 0, i64 0))
  %comp1 = icmp eq i32 %.2, 0
  br i1 %comp1, label %end, label %cycle

cycle:                                            ; preds = %entry, %cycle
  %i.02 = phi i32 [ %.17, %cycle ], [ 0, %entry ]
  %0 = sext i32 %i.02 to i64
  %.14 = getelementptr i8*, i8** %.1, i64 %0
  %.15 = load i8*, i8** %.14, align 8
  %.16 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.3, i64 0, i64 0), i8* %.15)
  %.17 = add nuw i32 %i.02, 1
  %comp = icmp eq i32 %.17, %.2
  br i1 %comp, label %end, label %cycle

end:                                              ; preds = %cycle, %entry
  %.20 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.4, i64 0, i64 0))
  ret void
}

; Function Attrs: norecurse nounwind
define void @swap(i8** nocapture %.1, i32 %.2, i32 %.3) local_unnamed_addr #2 {
entry:
  %0 = sext i32 %.2 to i64
  %.10 = getelementptr i8*, i8** %.1, i64 %0
  %.11 = load i8*, i8** %.10, align 8
  %1 = sext i32 %.3 to i64
  %.18 = getelementptr i8*, i8** %.1, i64 %1
  %.19 = load i8*, i8** %.18, align 8
  store i8* %.19, i8** %.10, align 8
  store i8* %.11, i8** %.18, align 8
  ret void
}

; Function Attrs: nounwind
define void @b_sort(i8** nocapture %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %.7 = add i32 %.2, -1
  %comp3 = icmp eq i32 %.7, 0
  br i1 %comp3, label %end, label %cycle

cycle:                                            ; preds = %entry, %end.1
  %i.04 = phi i32 [ %.41, %end.1 ], [ 0, %entry ]
  %0 = xor i32 %i.04, -1
  %.15 = add i32 %0, %.2
  %comp.11 = icmp eq i32 %.15, 0
  br i1 %comp.11, label %end.1, label %cycle.1

cycle.1:                                          ; preds = %cycle, %merge
  %j.02 = phi i32 [ %.26, %merge ], [ 0, %cycle ]
  %1 = sext i32 %j.02 to i64
  %.22 = getelementptr i8*, i8** %.1, i64 %1
  %.23 = load i8*, i8** %.22, align 8
  %.26 = add nuw i32 %j.02, 1
  %2 = sext i32 %.26 to i64
  %.27 = getelementptr i8*, i8** %.1, i64 %2
  %.28 = load i8*, i8** %.27, align 8
  %.29 = tail call i32 @strcmp(i8* %.23, i8* %.28)
  %.30 = icmp sgt i32 %.29, 0
  br i1 %.30, label %then, label %merge

then:                                             ; preds = %cycle.1
  tail call void @swap(i8** nonnull %.1, i32 %j.02, i32 %.26)
  br label %merge

merge:                                            ; preds = %then, %cycle.1
  %comp.1 = icmp eq i32 %.26, %.15
  br i1 %comp.1, label %end.1, label %cycle.1

end.1:                                            ; preds = %merge, %cycle
  %.41 = add nuw i32 %i.04, 1
  %comp = icmp eq i32 %.41, %.7
  br i1 %comp, label %end, label %cycle

end:                                              ; preds = %end.1, %entry
  ret void
}

; Function Attrs: nounwind
define void @merge(i8** nocapture %.1, i32 %.2, i32 %.3, i32 %.4) local_unnamed_addr #0 {
entry:
  %.12 = sub i32 %.3, %.2
  %.13 = add i32 %.12, 1
  %.17 = sub i32 %.4, %.3
  %.20 = tail call i8* @calloc(i32 %.13, i32 8)
  %.21 = bitcast i8* %.20 to i8**
  %.24 = tail call i8* @calloc(i32 %.17, i32 8)
  %.25 = bitcast i8* %.24 to i8**
  %comp18 = icmp eq i32 %.13, 0
  br i1 %comp18, label %check.1.preheader, label %cycle

check.1.preheader:                                ; preds = %cycle, %entry
  %comp.116 = icmp eq i32 %.17, 0
  br i1 %comp.116, label %test.1.preheader, label %cycle.1

cycle:                                            ; preds = %entry, %cycle
  %i.019 = phi i32 [ %.42, %cycle ], [ 0, %entry ]
  %0 = sext i32 %i.019 to i64
  %.34 = getelementptr i8*, i8** %.21, i64 %0
  %.38 = add i32 %i.019, %.2
  %1 = sext i32 %.38 to i64
  %.39 = getelementptr i8*, i8** %.1, i64 %1
  %.40 = load i8*, i8** %.39, align 8
  store i8* %.40, i8** %.34, align 8
  %.42 = add nuw i32 %i.019, 1
  %comp = icmp eq i32 %.42, %.13
  br i1 %comp, label %check.1.preheader, label %cycle

test.preheader:                                   ; preds = %cycle.1
  %.717 = icmp slt i32 %.13, 1
  %.748 = icmp slt i32 %.17, 1
  %.769 = or i1 %.717, %.748
  br i1 %.769, label %test.1.preheader, label %cycle.2

cycle.1:                                          ; preds = %check.1.preheader, %cycle.1
  %j.017 = phi i32 [ %.55, %cycle.1 ], [ 0, %check.1.preheader ]
  %2 = sext i32 %j.017 to i64
  %.52 = getelementptr i8*, i8** %.25, i64 %2
  %.55 = add nuw i32 %j.017, 1
  %.57 = add i32 %.55, %.3
  %3 = sext i32 %.57 to i64
  %.58 = getelementptr i8*, i8** %.1, i64 %3
  %.59 = load i8*, i8** %.58, align 8
  store i8* %.59, i8** %.52, align 8
  %comp.1 = icmp eq i32 %.55, %.17
  br i1 %comp.1, label %test.preheader, label %cycle.1

test.1.preheader:                                 ; preds = %merge, %check.1.preheader, %test.preheader
  %i.1.0.lcssa = phi i32 [ 0, %test.preheader ], [ 0, %check.1.preheader ], [ %i.1.1, %merge ]
  %j.1.0.lcssa = phi i32 [ 0, %test.preheader ], [ 0, %check.1.preheader ], [ %j.1.1, %merge ]
  %k.0.lcssa = phi i32 [ %.2, %test.preheader ], [ %.2, %check.1.preheader ], [ %.114, %merge ]
  %.1204 = icmp slt i32 %i.1.0.lcssa, %.13
  br i1 %.1204, label %cycle.3, label %test.2.preheader

cycle.2:                                          ; preds = %test.preheader, %merge
  %k.012 = phi i32 [ %.114, %merge ], [ %.2, %test.preheader ]
  %j.1.011 = phi i32 [ %j.1.1, %merge ], [ 0, %test.preheader ]
  %i.1.010 = phi i32 [ %i.1.1, %merge ], [ 0, %test.preheader ]
  %4 = sext i32 %i.1.010 to i64
  %.80 = getelementptr i8*, i8** %.21, i64 %4
  %.81 = load i8*, i8** %.80, align 8
  %5 = sext i32 %j.1.011 to i64
  %.84 = getelementptr i8*, i8** %.25, i64 %5
  %.85 = load i8*, i8** %.84, align 8
  %.86 = tail call i32 @strcmp(i8* %.81, i8* %.85)
  %.87 = icmp slt i32 %.86, 1
  %6 = sext i32 %k.012 to i64
  %.91 = getelementptr i8*, i8** %.1, i64 %6
  br i1 %.87, label %then, label %else

then:                                             ; preds = %cycle.2
  store i8* %.81, i8** %.91, align 8
  %.98 = add i32 %i.1.010, 1
  br label %merge

else:                                             ; preds = %cycle.2
  store i8* %.85, i8** %.91, align 8
  %.110 = add i32 %j.1.011, 1
  br label %merge

merge:                                            ; preds = %else, %then
  %i.1.1 = phi i32 [ %.98, %then ], [ %i.1.010, %else ]
  %j.1.1 = phi i32 [ %j.1.011, %then ], [ %.110, %else ]
  %.114 = add i32 %k.012, 1
  %.71 = icmp sge i32 %i.1.1, %.13
  %.74 = icmp sge i32 %j.1.1, %.17
  %.76 = or i1 %.71, %.74
  br i1 %.76, label %test.1.preheader, label %cycle.2

test.2.preheader:                                 ; preds = %cycle.3, %test.1.preheader
  %k.1.lcssa = phi i32 [ %k.0.lcssa, %test.1.preheader ], [ %.135, %cycle.3 ]
  %.1411 = icmp slt i32 %j.1.0.lcssa, %.17
  br i1 %.1411, label %cycle.4, label %end.4

cycle.3:                                          ; preds = %test.1.preheader, %cycle.3
  %k.16 = phi i32 [ %.135, %cycle.3 ], [ %k.0.lcssa, %test.1.preheader ]
  %i.1.25 = phi i32 [ %.132, %cycle.3 ], [ %i.1.0.lcssa, %test.1.preheader ]
  %7 = sext i32 %k.16 to i64
  %.125 = getelementptr i8*, i8** %.1, i64 %7
  %8 = sext i32 %i.1.25 to i64
  %.128 = getelementptr i8*, i8** %.21, i64 %8
  %.129 = load i8*, i8** %.128, align 8
  store i8* %.129, i8** %.125, align 8
  %.132 = add nsw i32 %i.1.25, 1
  %.135 = add i32 %k.16, 1
  %.120 = icmp slt i32 %.132, %.13
  br i1 %.120, label %cycle.3, label %test.2.preheader

cycle.4:                                          ; preds = %test.2.preheader, %cycle.4
  %k.23 = phi i32 [ %.156, %cycle.4 ], [ %k.1.lcssa, %test.2.preheader ]
  %j.1.22 = phi i32 [ %.153, %cycle.4 ], [ %j.1.0.lcssa, %test.2.preheader ]
  %9 = sext i32 %k.23 to i64
  %.146 = getelementptr i8*, i8** %.1, i64 %9
  %10 = sext i32 %j.1.22 to i64
  %.149 = getelementptr i8*, i8** %.25, i64 %10
  %.150 = load i8*, i8** %.149, align 8
  store i8* %.150, i8** %.146, align 8
  %.153 = add nsw i32 %j.1.22, 1
  %.156 = add i32 %k.23, 1
  %.141 = icmp slt i32 %.153, %.17
  br i1 %.141, label %cycle.4, label %end.4

end.4:                                            ; preds = %cycle.4, %test.2.preheader
  tail call void @free(i8* %.20)
  tail call void @free(i8* %.24)
  ret void
}

; Function Attrs: nounwind
define void @mergeSort(i8** %.1, i32 %.2, i32 %.3) local_unnamed_addr #0 {
entry:
  %.10 = icmp sgt i32 %.3, %.2
  br i1 %.10, label %then, label %merge

then:                                             ; preds = %entry
  %.15 = sub i32 %.3, %.2
  %.16 = sdiv i32 %.15, 2
  %.17 = add i32 %.16, %.2
  tail call void @mergeSort(i8** %.1, i32 %.2, i32 %.17)
  %.25 = add i32 %.17, 1
  tail call void @mergeSort(i8** %.1, i32 %.25, i32 %.3)
  tail call void @merge(i8** %.1, i32 %.2, i32 %.17, i32 %.3)
  ret void

merge:                                            ; preds = %entry
  ret void
}

; Function Attrs: nounwind
define void @main() local_unnamed_addr #0 {
entry:
  %.2 = tail call i32 @readint()
  %.5 = tail call i8* @calloc(i32 %.2, i32 8)
  %.6 = bitcast i8* %.5 to i8**
  %comp3 = icmp eq i32 %.2, 0
  br i1 %comp3, label %end.1.critedge, label %cycle

cycle:                                            ; preds = %entry, %cycle
  %i.04 = phi i32 [ %.22, %cycle ], [ 0, %entry ]
  %.13 = tail call i8* @calloc(i32 200, i32 1)
  %.16 = tail call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.5, i64 0, i64 0), i8* %.13)
  %0 = sext i32 %i.04 to i64
  %.19 = getelementptr i8*, i8** %.6, i64 %0
  store i8* %.13, i8** %.19, align 8
  %.22 = add nuw i32 %i.04, 1
  %comp = icmp eq i32 %.22, %.2
  br i1 %comp, label %end, label %cycle

end:                                              ; preds = %cycle
  %.25 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @.6, i64 0, i64 0))
  tail call void @printarr(i8** %.6, i32 %.2)
  %.31 = add i32 %.2, -1
  tail call void @mergeSort(i8** %.6, i32 0, i32 %.31)
  %.33 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([43 x i8], [43 x i8]* @.7, i64 0, i64 0))
  tail call void @printarr(i8** %.6, i32 %.2)
  br i1 %comp3, label %end.1, label %cycle.1

cycle.1:                                          ; preds = %end, %cycle.1
  %i.1.02 = phi i32 [ %.47, %cycle.1 ], [ 0, %end ]
  %1 = sext i32 %i.1.02 to i64
  %.44 = getelementptr i8*, i8** %.6, i64 %1
  %.45 = load i8*, i8** %.44, align 8
  tail call void @free(i8* %.45)
  %.47 = add nuw i32 %i.1.02, 1
  %comp.1 = icmp eq i32 %.47, %.2
  br i1 %comp.1, label %end.1, label %cycle.1

end.1.critedge:                                   ; preds = %entry
  %.25.c = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @.6, i64 0, i64 0))
  tail call void @printarr(i8** %.6, i32 %.2)
  %.31.c = add i32 %.2, -1
  tail call void @mergeSort(i8** %.6, i32 0, i32 %.31.c)
  %.33.c = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([43 x i8], [43 x i8]* @.7, i64 0, i64 0))
  tail call void @printarr(i8** %.6, i32 %.2)
  br label %end.1

end.1:                                            ; preds = %cycle.1, %end.1.critedge, %end
  tail call void @free(i8* %.5)
  ret void
}

attributes #0 = { nounwind }
attributes #1 = { nounwind readonly }
attributes #2 = { norecurse nounwind }
