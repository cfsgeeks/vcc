% for codes in code:
<DTMFSend command="True">
	<DTMFString>{{codes}}</DTMFString>
</DTMFSend>
% end
% end
<DTMFSend>
	<Value>#</Value>
</DTMFSend>