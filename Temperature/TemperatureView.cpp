
// TemperatureView.cpp : implementation of the CTemperatureView class
//

#include "stdafx.h"
// SHARED_HANDLERS can be defined in an ATL project implementing preview, thumbnail
// and search filter handlers and allows sharing of document code with that project.
#ifndef SHARED_HANDLERS
#include "Temperature.h"
#endif

#include "TemperatureDoc.h"
#include "TemperatureView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CTemperatureView

IMPLEMENT_DYNCREATE(CTemperatureView, CView)

BEGIN_MESSAGE_MAP(CTemperatureView, CView)
	// Standard printing commands
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CTemperatureView::OnFilePrintPreview)
	ON_WM_CONTEXTMENU()
	ON_WM_RBUTTONUP()
END_MESSAGE_MAP()

// CTemperatureView construction/destruction

CTemperatureView::CTemperatureView()
{
	// TODO: add construction code here

}

CTemperatureView::~CTemperatureView()
{
}

BOOL CTemperatureView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: Modify the Window class or styles here by modifying
	//  the CREATESTRUCT cs

	return CView::PreCreateWindow(cs);
}

// CTemperatureView drawing

void CTemperatureView::OnDraw(CDC* /*pDC*/)
{
	CTemperatureDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	// TODO: add draw code for native data here
}


// CTemperatureView printing


void CTemperatureView::OnFilePrintPreview()
{
#ifndef SHARED_HANDLERS
	AFXPrintPreview(this);
#endif
}

BOOL CTemperatureView::OnPreparePrinting(CPrintInfo* pInfo)
{
	// default preparation
	return DoPreparePrinting(pInfo);
}

void CTemperatureView::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add extra initialization before printing
}

void CTemperatureView::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: add cleanup after printing
}

void CTemperatureView::OnRButtonUp(UINT /* nFlags */, CPoint point)
{
	ClientToScreen(&point);
	OnContextMenu(this, point);
}

void CTemperatureView::OnContextMenu(CWnd* /* pWnd */, CPoint point)
{
#ifndef SHARED_HANDLERS
	theApp.GetContextMenuManager()->ShowPopupMenu(IDR_POPUP_EDIT, point.x, point.y, this, TRUE);
#endif
}


// CTemperatureView diagnostics

#ifdef _DEBUG
void CTemperatureView::AssertValid() const
{
	CView::AssertValid();
}

void CTemperatureView::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CTemperatureDoc* CTemperatureView::GetDocument() const // non-debug version is inline
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CTemperatureDoc)));
	return (CTemperatureDoc*)m_pDocument;
}
#endif //_DEBUG


// CTemperatureView message handlers
