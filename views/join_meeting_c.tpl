<Command>
% for number in meeting:
<DTMFSend command="True">
	<DTMFString>{{number}}</DTMFString>
</DTMFSend>
% end
<DTMFSend command="True">
	<DTMFString>#</DTMFString>
</DTMFSend>
% if code is not "0000":
% time.sleep(3000)
% for codes in code:
<DTMFSend command="True">
	<DTMFString>{{codes}}</DTMFString>
</DTMFSend>
% end
% end
<DTMFSend command="True">
	<DTMFString>#</DTMFString>
</DTMFSend>
</Command>