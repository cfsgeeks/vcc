<Command>
% for number in meeting:
<DTMFSend>
	<Value>{{number}}</Value>
</DTMFSend>
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
</Command>