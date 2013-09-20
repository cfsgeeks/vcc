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
% for codes in code:
<DTMFSend command="True">
	<Value>{{codes}}</Value>
</DTMFSend>
% end
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
</Command>