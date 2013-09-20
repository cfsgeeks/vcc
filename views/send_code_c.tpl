<Command>
	% for number in code:
<DTMFSend command="True">
	<DTMFString>{{number}}</DTMFString>
</DTMFSend>
	% end
<DTMFSend>
	<DTMFString>#</DTMFString>
</DTMFSend>
</Command>