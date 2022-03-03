@pushd %~dp0
@set DIR=dir .\firmware/B
@set READ=.\xmos_tool\dfu_usb.exe read_version

@call :cmd %DIR%
@if "%result%"=="" (
	color 4
	echo=
	echo δ��⵽�̼�������
	echo=
	set /p show=��ȷ���̼��� xmos_tool�ļ����µ�firmware�ļ����ڣ�����
) else (
	echo ���ҵ��̼����̼��汾Ϊ%result:~-11,3%
	set /p show=�������豸��������س�������ʼˢ¼����
)

@:loop
	@cls
	@color 0F

	@call :cmd %DIR%
	@if "%result%"=="" (
		color 4
		echo=
		echo δ��⵽�̼�������
		echo=
		set /p show=��ȷ���̼��� xmos_tool�ļ����µ�firmware�ļ����ڣ�����
		goto :loop
	)

	@set new=%result%
	@call :getV
	@set new=%new:~0,3%
	@echo �̼��汾��%new%
	@echo=

	@call :cmd %READ%
	@if "%result:~1,1%"=="t" (
		color 4
		echo=
		echo δ�����豸 ������
		echo=
		@set /p show=�����Ӻ��豸���û��س�����������ˢ��: 
		goto :loop	
	)
	@set per=%result:~9%
	@set per_v=%per:~0,1%%per:~2,1%%per:~4,1%
	@echo �豸��ǰ�汾��%per_v%

	@if "%new%"=="%per_v%" (
		color 4
		echo=
		set /p show=�̼��汾���豸�汾һ�£�����
		goto :loop
	)

	@call :cmd %DIR%
	.\xmos_tool\dfu_usb.exe write_upgrade .\firmware\%result%

	.\xmos_tool\dfu_usb.exe reboot
	@echo �汾У����......
	@ping /n 3 127.0.0.1 >nul
	@ping /n 3 127.0.0.1 >nul

	@call :cmd %READ%
	@set v=%result:~9%

	@echo=

	@if "%v%"=="3.0.4" (
		color 4
		echo ��¼�������󣬰汾����Ϊ3.0.4 ������
		@echo=
		@set /p show=���û��س�����������ˢ��: 
	) else (
		color 2
		echo ��¼�ɹ�����ǰ�汾Ϊ%v% ������
		@echo=
		@set /p show=���л��豸���û��س�����������ˢ��: 
	)
@goto :loop

::��ȡִ������Ľ��
@:cmd
	@for /f "delims=" %%t in ('%1 %2') do @set result=%%t
@goto :eof

::ͨ���̼�����ȡ�汾��
@:getV
	@if not "%new:V=%"=="%new%" set new=%new:*V=%&goto :getV
@goto :eof