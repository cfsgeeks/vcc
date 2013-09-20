<Command>
% for number in meeting:
<DTMFSend>
	<Value>{{number}}</Value>
</DTMFSend>
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
% if code != "0000":
% for number in code:
<DTMFSend command="True">
	<Value>{{number}}</Value>
</DTMFSend>
% end
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
</Command>