<Command>
% for number in meeting:
<DTMFSend command="True">
	<Value>{{number}}</Value>
</DTMFSend>
% end
<DTMFSend command="True">
	<Value>#</Value>
</DTMFSend>
<DTMFSend command="True">
	<Value>#</Value>
</DTMFSend>
</Command>