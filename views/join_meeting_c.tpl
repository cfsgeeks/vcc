<Command>
% for number in meeting:
<DTMFSend command="True">
	<DTMFString>{{number}}</DTMFString>
</DTMFSend>
% end
<DTMFSend command="True">
	<DTMFString>#</DTMFString>
</DTMFSend>
% if code != "0000":
% for number in code:
<DTMFSend command="True">
	<DTMFString>{{number}}</DTMFString>
</DTMFSend>
% end
% end
<DTMFSend command="True">
	<DTMFString>#</DTMFString>
</DTMFSend>
</Command>