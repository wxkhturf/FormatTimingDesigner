Header (
	company("EMA Design Automation") 
	product("TimingDesigner") 
	rev("9.2") 
	file("c:\\users\\administrator\\desktop\\test\\formattimingdesigner\\test - ¸±±¾.td") 
	date("10/30/2023") time("16:48") 
	format("9.0") 
	baseScale(1000.000000) 
	zoomFactor("0.000989843") 
	zoomBegin(0) 
	zoomEnd(478798) 
	nameFrameWidth(69) 
	simHDL(Verilog) 
	simDelayMechanism(Transport) 
	nextID(54) 
	TimingAnalysisMethod(51) 
	SDCVersion(0) 
	
	generalPrintParams( "printer,,,portrait,clipboard,Letter,default,6,5,in,color,scaleable,mifframe,preview,")
	diagramPrintParams( "0,2147483647,0,-1,true,true,1,1,true,true,true,true,all,diagramEnd")
	spreadsheetPrintParams( "0,2147483647,true,false,1,true,all")
	)
tclPreferences (UseAboveSixtyFiveNm UseAlteraFastTimingModel 
	UseActelMaxTimingModel UseTimingPath UseArrivalTime )
HDLHeader( 
	hdlFile("") 
	checkConstraints(true) 
	comment("") 
	checkTimeout(never) 
	
	command( name("test") cmdType(null) ))
DefaultLabel(
	delay(showNameString,"") 
	constraint(showNameString,"") 
	guarantee(showNameString,"") 
	measure(showMeasure,"") 
	store(showNameString,"") 
	wait(showNameString,"") 
	end(showNameString,"") 
	boundary(showIncrement,"") 
	loop(showNameString,"") 
	waveform(showSkip,"","") 
	specifiedclock(showSkip,"","") 
	derivedclock(showSkip,"","") 
	simwaveform(showSkip,"","") 
	bus(showValue,"","H") 
	)
DiagramStyle (
	waveformFont(winFont("Arial",90) qtFont("Arial",9) ) 
	rulerFont(winFont("Arial",90) qtFont("Arial",9) ) 
	relationshipFont(winFont("Arial",90) qtFont("Arial",9) ) 
	labelFont(winFont("Arial",90) qtFont("Arial",9) ) 
	annotationFont(winFont("Arial",80) qtFont("Arial",8) ) 
	slotHeight("11") 
	edgeHeight("11") 
	edgeGrade("1.96261") 
	inputPenStyle(0) 
	outputPenStyle(0) 
	inoutPenStyle(0) 
	internalPenStyle(0) 
	vRelationshipPenStyle(0) 
	hRelationshipPenStyle(0) 
	inputPenColor(3) 
	outputPenColor(3) 
	inoutPenColor(3) 
	internalPenColor(3) 
	wavePenWidth("0") 
	relationshipPenWidth("0") 
	wavesOnTop 
	relationshipsOnTop 
	annotationsOnTop 
	showSlopedEdges 
	edgeDisplayType(Uncertainty) 
	)
Waveform ( objectID(2) name("sig1") minheight("0") edges(
	(low,0.000,0.000,L), 
	(high,84000.000,84000.000), 
	(low,149000.000,149000.000), 
	(high,210000.000,210000.000), 
	(low,280000.000,280000.000), 
	(high,347000.000,347000.000), 
	(low,409000.000,409000.000), 
	(high,451000.000,451000.000), 
	(blank,453135.104,453135.104)) 
	hdl( direction(internal) ) label(showDefault,"","H") )
Bus ( objectID(3) name("sig2") minheight("0") edges(
	(valid,0.000,0.000,L,label(showText,"1","") ), 
	(z,41000.000,41000.000), 
	(valid,128000.000,128000.000,label(showText,"abcdefg","") ), 
	(z,166000.000,166000.000), 
	(valid,278000.000,278000.000,label(showText,"hijklmn","") ), 
	(z,332000.000,332000.000), 
	(valid,399000.000,399000.000,label(showText,"opqrst","") ), 
	(invalid,436000.000,436000.000), 
	(valid,454000.000,454000.000), 
	(blank,456135.104,456135.104)) 
	hdl( direction(internal) ) label(showDefault,"","H") )
Clock ( objectID(4) name("clk1") minheight("0") periodScale(1000.000) period(50.000000) dutyCycle(50.000000) 
	hdl( direction(internal) ) label(showDefault,"","H") )
DerivedClock ( objectID(5) name("clk2") minheight("0") referenceClock("clk1") dutyCycle(50.000000) removeCommonUncertaintyLike removeCommonUncertaintyUnlike 
	hdl( direction(internal) ) label(showDefault,"","H") )
EndCycleEvent ( objectID(1) name("end") time(454.472083) showVert hideOnPrinter label(showDefault,"") fromLatestEnd toEarliestBegin  )
