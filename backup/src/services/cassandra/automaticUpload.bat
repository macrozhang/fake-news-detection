@echo off

echo                                      Git�Զ����½ű�
echo ===================================================================================
echo.

set /p change=������Git���±䶯��
echo.
cd "D:\\AllCode\GitHub\\FaNed\\FaNed\\fake-news-detection"

git pull
git add .
git commit -m %change%
git push

echo.
echo ===================================================================================
echo                                      �������
echo.

pause
