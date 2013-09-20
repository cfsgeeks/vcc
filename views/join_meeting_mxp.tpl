<Command>
% for number in meeting:
<DTMFSend>
	<Value>{{number}}</Value>
</DTMFSend>
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
% if code is not "0000":
% for codes in code:
<DTMFSend command="True">
	<DTMFString>{{codes}}</DTMFString>
</DTMFSend>
% end
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>
</Command>