<Command>
% for number in meeting:
<DTMFSend command="True">
	<DTMFString>{{number}}</DTMFString>
</DTMFSend>
% end
<DTMFSend command="True">
	<DTMFString>#</DTMFString>
</DTMFSend>
<DTMFSend command="True">
	<DTMFString>#</DTMFString>
</DTMFSend>
</Command>